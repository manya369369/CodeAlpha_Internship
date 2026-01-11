def interactive_chatbot():
    print("Welcome to a User-Friendly Chatbot!")
    print("Type Bye to exit conservation")
    while True:
        user_input=input("You: ").lower().strip()
        if user_input=="bye":
            print("Chatbot: Goodbye!")
            break
        elif user_input in ["hi","hello","hey"]:
            print("Chatbot: Hi!")
        elif user_input=="how are you":
            print("Chatbot: I'm fine, thanks!")    
        else:
            print("Chatbot: I'm sorry, I don't understand that.But that seems to be fascinating and I wil gain more insights on it")  
interactive_chatbot()              
        