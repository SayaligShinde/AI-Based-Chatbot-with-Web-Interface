import sys
from datetime import datetime
import random

# Get user input from command line
user_input = sys.argv[1].lower()

# Define responses
greetings = ["hi", "hello", "hey", "good morning", "good evening"]
goodbyes = ["bye", "goodbye", "see you", "take care"]
how_are_you = ["how are you", "how's it going", "how are you doing"]
name_questions = ["what is your name", "who are you"]
time_questions = ["what time is it", "tell me the time", "current time"]
date_questions = ["what's the date", "what day is it", "tell me the date"]
jokes = [
    "Why don't programmers like nature? It has too many bugs.",
    "Why did the developer go broke? Because he used up all his cache.",
    "Why do Python programmers wear glasses? Because they can't C."
]

# Logic
if any(greet in user_input for greet in greetings):
    print("Hello! How can I assist you today?")
elif any(bye in user_input for bye in goodbyes):
    print("Goodbye! Have a great day 😊")
elif any(q in user_input for q in how_are_you):
    print("I'm just a bunch of code, but I'm feeling fantastic!")
elif any(q in user_input for q in name_questions):
    print("I'm your AI chatbot, created by a Computer Engineering student 😎")
elif any(q in user_input for q in time_questions):
    print("🕒 The current time is:", datetime.now().strftime("%I:%M %p"))
elif any(q in user_input for q in date_questions):
    print("📅 Today's date is:", datetime.now().strftime("%A, %B %d, %Y"))
elif "joke" in user_input or "funny" in user_input:
    print(random.choice(jokes))
elif "project" in user_input:
    print("I'm a mini AI chatbot project using Python, PHP, and a Web Interface.")
elif "creator" in user_input or "developer" in user_input:
    print("I was developed by a Computer Engineering student passionate about AI and web development.")
else:
    print("I'm still learning. Try asking something simple like 'hello', 'time', or 'joke'.")
