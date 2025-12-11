import json
import boto3
import urllib.request
import os
from datetime import datetime

# Initialize AWS clients
polly = boto3.client("polly")
s3 = boto3.client("s3")

# Set your variables
WEATHER_API_KEY = "55a0cf17128ccf80b269ec4ca43eefb6"
S3_BUCKET = "weather-voice-audio-output"  # your S3 bucket name

def lambda_handler(event, context):

    # Handle CORS preflight
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
                "Access-Control-Allow-Headers": "*",
            },
            "body": json.dumps({"message": "OK"}),
        }

    # Read city from query parameter
    params = event.get("queryStringParameters") or {}
    city = params.get("city", "Delhi")

    # Fetch weather
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    try:
        with urllib.request.urlopen(weather_url) as response:
            weather_data = json.loads(response.read().decode())
    except:
        return send_response(400, {"error": f"Unable to fetch weather for {city}"})

    # Parse important weather data
    temp = weather_data["main"]["temp"]
    feels = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    desc = weather_data["weather"][0]["description"].capitalize()

    # Generate natural sentence
    text = (
        f"Here is the weather update for {city}. "
        f"The temperature is {temp} degrees Celsius, "
        f"feels like {feels}. Humidity is {humidity} percent. "
        f"Overall, the weather is {desc}."
    )

    # Convert text to speech using Polly
    audio_stream = polly.synthesize_speech(
        Text=text,
        VoiceId="Joanna",
        OutputFormat="mp3"
    )["AudioStream"].read()

    # Generate unique filename
    file_name = f"weather-{city}-{datetime.utcnow().timestamp()}.mp3"

    # Upload to S3
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=file_name,
        Body=audio_stream,
        ContentType="audio/mpeg",
        ACL="public-read"
    )

    audio_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{file_name}"

    return send_response(200, {
        "city": city,
        "weather": desc,
        "temperature": temp,
        "humidity": humidity,
        "message": text,
        "audio_url": audio_url
    })


def send_response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*"
        },
        "body": json.dumps(body)
    }
