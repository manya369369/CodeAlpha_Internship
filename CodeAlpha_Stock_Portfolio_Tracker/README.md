Project Overview-
  This project is a Python-based Stock Portfolio Tracker developed as part of the Python Programming Internship at CodeAlpha. The goal of the project is to demonstrate proficiency in data organization using dictionaries, user input handling, and performing arithmetic operations to solve real-world financial tracking problems.
Task Description-
  The objective of Task 2 is to create a functional tool that tracks a user's stock investment value based on current market prices. To meet the specific requirements of the internship, the project follows these guidelines:
Data Storage: The program utilizes a hardcoded dictionary to maintain stock symbols         and their corresponding prices.
User Interaction: The user provides the stock symbol and the number of shares they own.
Output Generation: The program calculates the total portfolio value and provides a clear    summary to the user, with an option to save the data to a file.
Technical Implementation-
The program is built using several key Python concepts to ensure efficient logic and accurate calculations:
Dictionaries: Acts as the core database to store stock symbols as keys and their unit prices as values for quick lookup.
Arithmetic Operations: Implements mathematical logic to multiply unit prices by user-provided quantities to determine total investment value.
Input Validation: Uses conditional statements to verify if a stock symbol entered by the user exists within the predefined dictionary.
File Handling: Utilizes Python's built-in file writing capabilities to export the portfolio summary into a permanent text report.
How the Program Works
Data Initialization: The program loads a dictionary containing various stock symbols (e.g., AAPL, TSLA, MSFT) and their fixed prices.
User Input: The user is prompted to enter the ticker symbol of the stock they own and the total number of shares.
Lookup and Calculation: The system searches the dictionary for the entered symbol. If found, it retrieves the price and multiplies it by the number of shares.
Result Output: The total valuation is displayed on the console and automatically written into a file named portfolio_report.txt for the user's records.
Installation and Usage
Ensure you have Python 3.x installed on your system.
Clone the repository: git clone https://github.com/YourUsername/CodeAlpha_StockTracker.
Navigate to the directory and run the script: python main.py.