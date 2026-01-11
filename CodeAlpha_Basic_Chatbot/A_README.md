Project Overview:
   This project is a Python-based implementation of a rule-based Chatbot, developed as part of the Python Programming Internship at CodeAlpha. The goal of the     project is to demonstrate proficiency in natural language processing (NLP) basics, string manipulation, and the implementation of interactive control flow loops.
Task Description:
 The objective of Task 4 is to create a functional conversational agent that can interact with users through the console. To meet the specific requirements of the    internship, the project follows these guidelines:
  1.Interaction Model: The chatbot operates on a predefined set of rules to respond to user queries.
  2.Continuous Conversation: The program utilizes a loop to allow multiple interactions until the user chooses to exit.
  3.Scope: The bot is designed to handle common greetings, answer basic questions, and provide a polite sign-off.
Technical Implementation:
 The program is built using several key Python concepts to ensure a smooth and responsive user experience:
  1.Conditional Logic (if-elif-else): Acts as the "brain" of the chatbot, matching user keywords to specific predefined responses.
  2.String Normalization: Uses methods like .lower() and .strip() to ensure that user inputs are processed correctly regardless of capitalization or extra spaces.
  3.Infinite Loops (while True): Enables the chatbot to remain active and "listening" for the next user input without the script ending prematurely.
  4.Pattern Matching: Implements basic keyword detection to simulate a real conversation based on the context of the user's message.
How the Chatbot Works:
  1.Startup: The program initializes and displays a welcoming message, informing the user how to interact and how to exit (e.g., by typing 'bye').
  2.User Input: The system waits for the user to type a message into the console.
  3.Processing: The chatbot converts the input to lowercase and checks it against a dictionary or a series of conditional statements.
  4.Response Generation: - If a keyword is recognized (e.g., "hello"), a matching response is printed.
  5.If the input is unrecognized, a "fallback" response is provided, asking the user to rephrase.
  6.Termination: If the user types a termination keyword (e.g., "exit", "bye", or "quit"), the loop breaks, and a final goodbye message is displayed.
Installation and Usage:
 1.Ensure you have Python 3.14.2 installed on your system.
 2.Clone the repository: git clone https://github.com/YourUsername/CodeAlpha_BasicChatbot.
 3.Navigate to the directory and run the script: python main.py.
