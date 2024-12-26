import random
responses = {
    "greetings": ["Hi there!", "Hello!", "Hey! How can I help you?", "Hi! What's up?"],
    "how_are_you": [
        "I'm just a bot, but I'm doing great! How about you?",
        "All systems are running smoothly. How are you?",
    ],
    "bye": [
        "Goodbye! Take care!",
        "See you later! Have a great day!",
        "Bye! It was nice talking to you!",
    ],
    "default": [
        "I'm not sure I understand that. Can you rephrase?",
        "Sorry, I don't have an answer for that.",
        "Interesting! Tell me more.",
    ],
}

keywords = {
    "hello": "greetings",
    "hi": "greetings",
    "hey": "greetings",
    "how are you": "how_are_you",
    "bye": "bye",
    "exit": "bye",
    "quit": "bye",
}
def get_response(user_input):
    user_input = user_input.lower()
    for key in keywords:
        if key in user_input:
            category = keywords[key]
            return random.choice(responses[category])
    return random.choice(responses["default"])

def chatbot():
    print("Chatbot: Hello! I'm your assistant chatbot. Type 'bye', 'exit', or 'quit' to end the chat.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot:", random.choice(responses["bye"]))
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
