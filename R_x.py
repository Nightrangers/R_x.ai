import random
import emoji
import json

class R_X:
    def __init__(self, name="R_X"):
        self.name = name
        self.memory = {}  # Store conversation history and user preferences
        self.knowledge_base = {
            "weather": "I'm still learning about weather patterns. Could you tell me your location?",
            "hello": "Hi there! 👋 How can I assist you today?",
            "thank you": "You're very welcome! 😊",
            "favorite color": "That’s interesting! 🌈",
            "who are you": f"My name is {self.name} and I’m here to chat! 🤖"
        }

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Check memory first
        if user_input in self.memory:
            return self.memory[user_input]

        # Check knowledge base
        if user_input in self.knowledge_base:
            response = self.knowledge_base[user_input]
            if any(emoji.emoji_codes[e] for e in response): # Check if the response contains emojis
                response = emoji.emojize(response)
            self.memory[user_input] = response  # Store the response in memory
            return response

        # Default response
        responses = [
            "That’s an interesting point. 🤔 Let me think about that...",
            "I'm processing your request. ⏳ Give me a moment.",
            "Could you elaborate on that? 🗣️"
        ]
        response = random.choice(responses)
        if any(emoji.emoji_codes[e] for e in response):
            response = emoji.emojize(response)
        self.memory[user_input] = response  # Store in memory
        return response

    def save_memory(self):
        with open("memory.json", "w") as f:
            json.dump(self.memory, f)

    def load_memory(self):
        try:
            with open("memory.json", "r") as f:
                self.memory = json.load(f)
        except FileNotFoundError:
            self.memory = {}

# Main interaction loop
if __name__ == "__main__":
    rx = R_X()
    rx.load_memory()
    rx.save_memory() #Save it on start

    print(f"{rx.name}: Hello! 👋  How can I help you? (Type 'exit' to quit)")

    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            print(f"{rx.name}: Goodbye! 👋")
            break

        response = rx.get_response(user_input)
        print(f"{rx.name}: {response}")


