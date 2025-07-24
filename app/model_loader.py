import joblib
import re
import string
import os
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def predict_category(text: str) -> str:
    cleaned = text.lower()
    cleaned = re.sub(r"http\S+", "", cleaned)
    cleaned = re.sub(r"[^a-z0-9\s]", "", cleaned)
    vec = vectorizer.transform([cleaned])
    return model.predict(vec)[0]
