from flask import Flask, request, jsonify
from datetime import datetime
import random
from flask_cors import CORS
CORS(app)

app = Flask(__name__)

# Sample responses
jokes = [
    "Why don't programmers like nature? Too many bugs.",
    "Why did the developer go broke? Because he used up all his cache.",
    "Why do Python programmers wear glasses? Because they can't C."
]

@app.route("/")
def home():
    return "AI Chatbot Flask API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    if "hello" in user_input or "hi" in user_input:
        return jsonify(response="Hello! How can I help you today?")
    elif "how are you" in user_input:
        return jsonify(response="I'm just code, but I'm doing great!")
    elif "time" in user_input:
        return jsonify(response=f"The current time is {datetime.now().strftime('%I:%M %p')}")
    elif "date" in user_input or "day" in user_input:
        return jsonify(response=f"Today's date is {datetime.now().strftime('%A, %B %d, %Y')}")
    elif "joke" in user_input:
        return jsonify(response=random.choice(jokes))
    else:
        return jsonify(response="I'm still learning. Try asking about time, date, or a joke!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
