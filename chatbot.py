# -----------------------------------------
# Task 4: Basic Rule-Based Chatbot
# -----------------------------------------

def get_response(user_input):
    """
    This function takes user input and
    returns an appropriate chatbot response.
    """

    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! Nice to meet you."
    
    elif user_input == "hi":
        return "Hello! How can I help you?"
    
    elif user_input == "how are you":
        return "I'm fine, thanks for asking!"
    
    elif user_input == "what is your name":
        return "I am a simple rule-based chatbot."
    
    elif user_input == "what can you do":
        return "I can chat with you using predefined rules."
    
    elif user_input == "help":
        return "You can say hello, ask how I am, or say bye to exit."
    
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    
    else:
        return "Sorry, I don't understand that."


def chatbot():
    """
    Main chatbot function that runs continuously
    until the user types 'bye'.
    """

    print("====================================")
    print("        BASIC CHATBOT STARTED        ")
    print("====================================")
    print("Type 'bye' to exit the chatbot.\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower() == "bye":
            break


# Program execution starts here
if __name__ == "__main__":
    chatbot()
