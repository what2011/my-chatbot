import json
import os

# Load or initialize the chatbot memory
if os.path.exists("memory.json"):
    with open("memory.json", "r") as f:
        memory = json.load(f)
else:
    memory = {}

def save_memory():
    with open("memory.json", "w") as f:
        json.dump(memory, f)

def chat():
    print("🤖 Chatbot: Hello! I can learn. Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("🤖 Chatbot: Goodbye!")
            break

        if user_input in memory:
            print("🤖 Chatbot:", memory[user_input])
        else:
            response = input("🤖 I don't know how to reply. What should I say? ")
            memory[user_input] = response
            save_memory()
            print("🤖 Chatbot: Got it! I'll remember that.")

if __name__ == "__main__":
    chat()
