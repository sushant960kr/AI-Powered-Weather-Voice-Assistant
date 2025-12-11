<h1 align="center">🌦️🎤 AI-Powered Weather Voice Assistant</h1>
<h3 align="center">AWS Serverless • Amazon Polly • Lambda • API Gateway • S3 • DynamoDB • OpenWeather API</h3>
<hr/>

<h2>📌 Project Overview</h2>
<p>
The <b>AI-Powered Weather Voice Assistant</b> is a completely serverless cloud application that converts real-time weather data into <b>natural human speech</b> using <b>Amazon Polly</b>.
<br/><br/>
A user enters a city name → the backend fetches weather details → generates an MP3 audio → stores it in Amazon S3 → returns a <b>presigned URL</b> to the frontend for playback.
</p>
<p>This project demonstrates <b>Serverless, AI, Cloud, API integration, and Frontend development</b> in one practical solution.</p>

<hr/>

<h2>🧰 Tech Stack</h2>

<h3>Frontend</h3>
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>

<h3>Backend (Serverless)</h3>
<ul>
  <li>AWS Lambda (Python)</li>
  <li>Amazon API Gateway</li>
  <li>Amazon Polly</li>
  <li>Amazon S3</li>
  <li>Amazon DynamoDB (Weather logs)</li>
  <li>IAM Roles & Permissions</li>
  <li>OpenWeather API</li>
</ul>

<hr/>

<h2>📡 Architecture</h2>

<pre>
User → Frontend → API Gateway → Lambda
→ OpenWeather API → Polly → S3 (MP3 audio)
→ DynamoDB (Logs) → Presigned URL → Frontend audio player
</pre>

<hr/>

<h2>🚀 Features</h2>
<ul>
  <li>✔ Converts weather text to high-quality speech</li>
  <li>✔ Gets real-time weather from OpenWeather API</li>
  <li>✔ MP3 stored securely in Amazon S3</li>
  <li>✔ Presigned URLs allow 1-hour secure playback</li>
  <li>✔ Modern responsive frontend interface</li>
  <li>✔ Fully serverless architecture (no servers to manage)</li>
  <li>✔ DynamoDB logs all weather queries</li>
</ul>

<hr/>

<h2>⚙️ AWS Setup</h2>

<ol>
  <li>Create S3 Bucket</li>
  <li>Create DynamoDB Table</li>
  <li>Create IAM Role for Lambda</li>
  <li>Create AWS Lambda Function</li>
  <li>Configure Amazon Polly + S3 Access</li>
  <li>Create API Gateway → Connect to Lambda</li>
  <li>Enable CORS</li>
  <li>Deploy Frontend to S3 (Static Website Hosting)</li>
</ol>

<hr/>

<h2>🎯 Why This Project Is Perfect for Resume</h2>

<ul>
  <li>✔ Demonstrates Serverless Architecture</li>
  <li>✔ Real-world API Integration</li>
  <li>✔ Uses AI/ML (Amazon Polly)</li>
  <li>✔ Combines Frontend + Backend + Cloud</li>
  <li>✔ Implements Security (IAM + Presigned URLs)</li>
  <li>✔ Includes Logging, Monitoring, Scalability</li>
</ul>

<hr/>

<h2>📸 Screenshots</h2>

<img width="1917" alt="Screenshot 2025-12-11 141807" src="https://github.com/user-attachments/assets/dbd7ab46-8dbf-4b83-82b0-665f41374673" />

<img width="1915" alt="Screenshot 2025-12-11 141702" src="https://github.com/user-attachments/assets/524760e6-941c-4075-981d-853400cbdfaf" />

<img width="1912" alt="Screenshot 2025-12-11 141846" src="https://github.com/user-attachments/assets/459c3c54-c436-40cb-a02f-3c1c1f520385" />


<hr/>

<h2>📘 Future Enhancements</h2>
<ul>
  <li>🎤 Add microphone-based voice input</li>
  <li>🗣️ Add Amazon Transcribe (Speech → Text)</li>
  <li>🌍 Support multiple Polly voices & languages</li>
  <li>⚠️ Add weather alerts</li>
  <li>📱 Build a mobile app version</li>
</ul>

<hr/>

<h2>👨‍💻 Author</h2>
<p><b>Sushant Kumar</b><br/>
Cloud • DevOps • MERN • AWS • Serverless
</p>
