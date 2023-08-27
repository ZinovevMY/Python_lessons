from allmodules import portfolio as p


start_stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
start_prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
current_stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
current_prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}

initial_value = p.calculate_portfolio_value(start_stocks, start_prices)
current_value = p.calculate_portfolio_value(current_stocks, current_prices)
profitability = p.calculate_portfolio_return(initial_value, current_value)
profit_company = p.get_most_profitable_stock(start_prices, current_prices)

print(initial_value)
print(current_value)
print(f'{profitability: .2f}%')
print(profit_company)