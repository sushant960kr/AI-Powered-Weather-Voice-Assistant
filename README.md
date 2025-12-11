🌦️🎤 AI-Powered Weather Voice Assistant
AWS Serverless • Amazon Polly • Lambda • API Gateway • S3 • DynamoDB • OpenWeather API
📌 Project Overview
The AI-Powered Weather Voice Assistant is a fully serverless cloud application that converts real-time weather data into natural human voice using Amazon Polly.
A user enters a city name → backend fetches weather details → generates an MP3 audio → stores in S3 → returns a presigned URL to the frontend for playback.
This project demonstrates Serverless, AI, Cloud, API integration, and front-end development in one practical solution.

🧰 Tech Stack
-> Frontend
-> HTML
-> CSS
-> JavaScript
-> Backend (Serverless)
-> AWS Lambda (Python)
-> Amazon API Gateway
-> Amazon Polly
-> Amazon S3
-> Amazon DynamoDB (logging)
-> IAM Roles & Policies
-> OpenWeather API

📡 How It Works (Architecture)
User → Frontend → API Gateway → Lambda
→ OpenWeather API → Polly → S3 (MP3 audio)
→ DynamoDB (Logs) → Presigned URL → Frontend audio player

🚀 Features

✔ Converts weather text to high-quality speech
✔ Real-time weather from OpenWeather API
✔ MP3 stored securely in Amazon S3
✔ Presigned URL allows 1-hour playback
✔ Modern frontend interface
✔ Serverless architecture (zero servers to manage)
✔ Logs weather queries to DynamoDB

⚙️ AWS Setup
1. Create S3 Bucket
2. Create DynamoDB Table
3. IAM Role for Lambda
4. Create AWS Lambda Function
5. Add API Gateway
6. Frontend Setup in S3

🎯 Why This Project Is Great for Resume
This project showcases:
-> AWS Serverless Architecture
-> Real-world API integration
-> AI/ML (Amazon Polly)
-> Frontend + Backend + Cloud + DevOps
-> Security (IAM, presigned URLs)
-> Logging and monitoring

📸 Screenshots

<img width="1917" height="1139" alt="Screenshot 2025-12-11 141807" src="https://github.com/user-attachments/assets/dbd7ab46-8dbf-4b83-82b0-665f41374673" />
<img width="1915" height="1098" alt="Screenshot 2025-12-11 141702" src="https://github.com/user-attachme<img width="1915" height="1098" alt="Screenshot 2025-12-11 141702" src="https://github.com/user-attachments/assets/524760e6-941c-4075-981d-853400cbdfaf" />
<img width="1912" height="1139" alt="Screenshot 2025-12-11 141846" src="https://github.com/user-attachments/assets/459c3c54-c436-40cb-a02f-3c1c1f520385" />
nts/assets/d0182be2-6a77-4e44-8ff9-c173794f77d4" />
<img width="1917" height="1139" alt="Screenshot 2025-12-11 141807" src="https://github.com/user-attachments/as<img width="1917" height="1139" alt="Screenshot 2025-12-11 141807" src="https://github.com/user-attachments/assets/26803956-d571-4aa3-9fd1-783aedae12c2" />
sets/d485499f-8f92-4110-b2a0-a00417637810" />


📘 Future Enhancements

-> Add microphone-based input
-> Add Amazon Transcribe for speech-to-text
-> Multi-language voice support
-> Add weather alerts
-> Build mobile version

👨‍💻 Author
Sushant Kumar
Cloud • DevOps • MERN • AWS • Serverless
