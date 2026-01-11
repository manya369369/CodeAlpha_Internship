Project Overview-
  This project is a Python-based Stock Portfolio Tracker developed as part of the Python Programming Internship at CodeAlpha. The goal of the project is to demonstrate proficiency in data organization using dictionaries, user input handling, and performing arithmetic operations to solve real-world financial tracking problems.
Task Description-
 The objective of Task 2 is to create a functional tool that tracks a user's stock investment value based on current market prices. To meet the specific              requirements of the internship, the project follows these guidelines:
  1.Data Storage: The program utilizes a hardcoded dictionary to maintain stock symbols and their corresponding prices.
  2.User Interaction: The user provides the stock symbol and the number of shares they own.
  3.Output Generation: The program calculates the total portfolio value and provides a clear summary to the user, with an option to save the data to a file.
Technical Implementation-
  The program is built using several key Python concepts to ensure efficient logic and accurate calculations:
   1.Dictionaries: Acts as the core database to store stock symbols as keys and their unit prices as values for quick lookup.
   2.Arithmetic Operations: Implements mathematical logic to multiply unit prices by user-provided quantities to determine total investment value.
   3.Input Validation: Uses conditional statements to verify if a stock symbol entered by the user exists within the predefined dictionary.
   4.File Handling: Utilizes Python's built-in file writing capabilities to export the portfolio summary into a permanent text report.
How the Program Works-
  1.Data Initialization: The program loads a dictionary containing various stock symbols (e.g., AAPL, TSLA, MSFT) and their fixed prices.
  2.User Input: The user is prompted to enter the ticker symbol of the stock they own and the total number of shares.
  3.Lookup and Calculation: The system searches the dictionary for the entered symbol. If found, it retrieves the price and multiplies it by the number of shares.
  4.Result Output: The total valuation is displayed on the console and automatically written into a file named portfolio_report.txt for the user's records.
Installation and Usage-
  1.Ensure you have Python 3.14.2 installed on your system.
  2.Clone the repository: git clone https://github.com/YourUsername/CodeAlpha_StockTracker.
  3.Navigate to the directory and run the script: python main.py.
