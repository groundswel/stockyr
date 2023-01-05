# Import libraries
import pandas as pd
import yfinance as yf
from sklearn.linear_model import LinearRegression

# Get the ticker symbol from the user
symbol = input("Enter the ticker symbol: ")

# Download the stock data from Yahoo Finance
data = yf.Ticker(symbol).history(period="5y")

# Extract the stock prices as a numpy array
X = data["Date"].values.reshape(-1, 1)
y = data["Close"].values

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict the stock price for the next two weeks
predictions = model.predict(np.array([[21], [22], [23], [24], [25], [26], [27]]).reshape(-1, 1))

# Calculate the minimum and maximum predicted price
min_price = min(predictions)
max_price = max(predictions)

# Print the predicted price range
print(f"The predicted price range for the next two weeks is ${min_price:.2f} to ${max_price:.2f}")
