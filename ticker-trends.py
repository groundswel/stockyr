import yfinance as yf
import pandas as pd

# Get a list of ticker symbols
ticker_symbols = ["AAPL", "GOOG", "MSFT", "FB", "AMZN", "TSLA", "UBER", "LYFT", "NOK", "SNE"]

# Download the stock data from Yahoo Finance
data = pd.DataFrame()
for symbol in ticker_symbols:
    data[symbol] = yf.Ticker(symbol).history(period="5y")["Close"]

# Calculate the percentage change in price over the past year
pct_change = data.pct_change(periods=252).iloc[-1]

# Sort the stocks by percentage change
sorted_stocks = pct_change.sort_values(ascending=False)

# Print the top 10 trending stocks
print(sorted_stocks.head(10))
