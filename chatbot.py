def chatbot():
    print("Hello! I'm a basic chatbot. Type 'bye' to exit. or say hello ")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot:  Goodbye! have a good day ")
            break
        elif "hello" in user_input:
            print("Chatbot: Hi there!")
        elif "how are you" in user_input:
            print("Chatbot:  I'm  fine and i am just a bunch of code, but I'm doing great!")
        else:
            print("Chatbot: I'm not sure how to respond to that.") 
            print("Namstey")    

chatbot()
