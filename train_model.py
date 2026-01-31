# train_model.py
import os
import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents from the JSON file
file_path = os.path.abspath("./intents_updated.json")
with open(file_path, "r", encoding="utf-8") as file:
    intents = json.load(file)

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Train the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

# Save the trained model and vectorizer using joblib
model_directory = 'chatbot_model'
os.makedirs(model_directory, exist_ok=True)

joblib.dump(clf, os.path.join(model_directory, 'clf.pkl'))
joblib.dump(vectorizer, os.path.join(model_directory, 'vectorizer.pkl'))

print("Model and vectorizer have been saved!")
