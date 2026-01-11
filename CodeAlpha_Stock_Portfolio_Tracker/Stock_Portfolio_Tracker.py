stock_prices={
    "AAPL":180,
    "TSLA":250,
    "GOOGL":140,
    "AMZN":175,
    "MSFT":400,
}
print("Welcome to the Stock Portfolio Tracker!")
stock_name=input("Enter the stock symbol you own: ").upper()
quantity=int(input(f"Enter the number of shares of {stock_name} you own: "))
if stock_name in stock_prices:
    price=stock_prices[stock_name]
    total_value=price*quantity
    with open("portfolio_report.txt","w") as file:
     file.write("Stock Portfolio Report")
     file.write(f"Stock:{stock_name}") 
     file.write(f"Quantity Owned: {quantity}")
     file.write(f"Current Price In Market: ${price}") 
     file.write(f"Total Invested Money: ${total_value}")  
    print("Report is succesfully saved to portfolio_report.txt")     
    print(f"Portfolio Summary:")
    print(f"Stock:{stock_name}")
    print(f"Current Price: ${price}")
    print(f"Quantity Owned: {quantity}")
    print(f"Total Investment Value: ${total_value}")
else:
    print(f"Sorry, {stock_name} is not found in our records.")  
