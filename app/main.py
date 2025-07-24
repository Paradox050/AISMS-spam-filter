from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.utils import is_whitelisted
from app.model_loader import predict_category

app = FastAPI()

class SMSInput(BaseModel):
    message: str

@app.post("/check_sms")
def check_sms(input_data: SMSInput):
    message = input_data.message

    allowed, reason = is_whitelisted(message)
    if allowed:
        return {"verdict": "allowed", "reason": "whitelisted"}

    category = predict_category(message)

    if category == "Spam":
        return {"verdict": "blocked", "reason": "ai"}
    else:
        return {"verdict": "allowed", "reason": "ai"}
