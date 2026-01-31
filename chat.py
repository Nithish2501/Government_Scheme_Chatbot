
import streamlit as st
import joblib
import json
import os
import random
import datetime
import csv
import nltk
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')
nltk.data.path.append(os.path.abspath("nltk_data"))

clf = joblib.load("chatbot_model/clf.pkl")
vectorizer = joblib.load("chatbot_model/vectorizer.pkl")

with open("intents_updated.json", encoding="utf-8") as f:
    intents = json.load(f)

def chatbot_response(user_input):
    input_vector = vectorizer.transform([user_input])
    tag = clf.predict(input_vector)[0]

    for intent in intents:
        if intent["tag"] == tag:
            responses = intent.get("responses")
            if isinstance(responses, dict):
                return responses.get("en", list(responses.values())[0])  # Use English or fallback
            elif isinstance(responses, list) and responses:
                return random.choice(responses)
            else:
                return "I found the topic, but no proper responses are configured."

    return "I'm sorry, I didn't understand that."





if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in first.")
    st.stop()

st.title(f"Welcome {st.session_state.username} - Government Scheme Chatbot")

user_input = st.text_input("You:")
if user_input:
    response = chatbot_response(user_input)
    st.text_area("Chatbot:", value=response, height=100)
    with open("chat_log.csv", "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([st.session_state.username, user_input, response, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
