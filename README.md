AI-Powered SMS Spam Filter for A2P Messaging
This project is an intelligent, lightweight AI solution that classifies A2P (Application-to-Person) SMS messages into:
Spam
Promotional
Transactional

Built using Scikit-learn, FastAPI, and Docker, this project exposes a RESTful API and includes a whitelisting mechanism to bypass known safe senders such as trusted domains or OTP templates.

📹 Loom Project Walkthrough
https://www.loom.com/share/aee28b2864354f41b5b2e22a86f1fe7e?sid=9bcfe867-7a2c-4d15-a3b2-e8a48918ff04


Model Used
Vectorizer: TfidfVectorizer
Classifier: Logistic Regression

Trained on: Labeled SMS dataset with categories (spam, transactional, promotional)

Whitelisting:
Before predicting a message category using the AI model, the system checks if the message contains any whitelisted terms such as:

Trusted domain names (trip.com, irctc, etc.)

Verified OTP message patterns

Internal shortcodes used by businesses

If a match is found, the message is immediately classified as transactional, regardless of the ML model’s output.

This adds a layer of safety and trust to the filtering mechanism, especially in high-volume enterprise use cases.


How to Run the API Locally
1. Clone the Repository
git clone https://github.com/your-username/ai-sms-spam-filter-api.git
cd ai-sms-spam-filter-api
Build Docker Image
docker build -t sms-spam-api .
Run Docker Container
docker run -d -p 8000:8000 sms-spam-api
Once the container is running, the live API will be available at:
http://localhost:8000/docs

How to Use the API
Endpoint: /predict
Method: POST
URL: http://localhost:8000/docs

Payload Format:
{
  "message": "Your OTP for login is 123456 - trip.com"
}
Response:
{
  "prediction": "allowed",
  "via": "whitelist"
}
Or for non-whitelisted messages:
{
  "prediction": "not allowed",
  "via": "model"
}
Use the FastAPI Swagger UI to test easily:

🔗 http://localhost:8000/docs

Requirements (for local setup without Docker)
pip install -r requirements.txt
Run locally:
uvicorn app.main:app --host 0.0.0.0 --port 8000

Features
✔️ AI-based classification for spam, promotional, and transactional messages

✔️ Whitelisting mechanism for trusted domains and templates

✔️ Clean REST API using FastAPI

✔️ Dockerized for deployment anywhere

✔️ Interactive Swagger docs at /docs

