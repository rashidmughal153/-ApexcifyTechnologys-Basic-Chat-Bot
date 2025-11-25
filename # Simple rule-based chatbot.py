# Simple rule-based chatbot

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

print("Welcome to Simple Chatbot! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    
    if user_input.lower() in ["bye", "goodbye", "see you"]:
        break
