import pandas as pd
import numpy as np
import joblib
import re
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (
    classification_report, accuracy_score, precision_score, recall_score,
    f1_score
)
from sklearn.preprocessing import LabelBinarizer


# Load dataset
df = pd.read_csv("message_dataset_50k.csv")

# Clean and preprocess
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)  
    text = re.sub(r"[^a-z0-9\s]", "", text)  
    return text.strip()

df['cleaned_message'] = df['Message'].apply(clean_text)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    df['cleaned_message'], df['Category'], test_size=0.2, random_state=42)

# Vectorize
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train
model = LogisticRegression(max_iter=300)
model.fit(X_train_vec, y_train)

# Evaluate
# shuffled_labels = np.random.permutation(y_train)
# model.fit(X_train_vec, shuffled_labels)

y_pred = model.predict(X_test_vec)
y_train_pred = model.predict(X_train_vec)

print("Train Accuracy:", accuracy_score(y_train, y_train_pred))
print("Test Accuracy:", accuracy_score(y_test, y_pred))

print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision (weighted):", precision_score(y_test, y_pred, average='weighted'))
print("Recall (weighted):", recall_score(y_test, y_pred, average='weighted'))
print("F1 Score (weighted):", f1_score(y_test, y_pred, average='weighted'))



# Save model and vectorizer
joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")
