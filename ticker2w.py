# Import libraries
import pandas as pd
import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression

# Get the ticker symbol from the user
symbol = input("Enter the ticker symbol: ")

# Download the stock data from Yahoo Finance
data = yf.Ticker(symbol).history(period="5y")

# Extract the input features and output as numpy arrays
X = data[["Open", "High", "Low", "Close", "Volume"]].values
y = data[["High", "Low"]].values

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict the stock high and low prices for the next two weeks
predictions = model.predict(np.array([[140, 150, 130, 140, 100000], [140, 150, 130, 140, 100000], [140, 150, 130, 140, 100000], [140, 150, 130, 140, 100000], [140, 150, 130, 140, 100000], [140, 150, 130, 140, 100000], [140, 150, 130, 140, 100000]]))

# Calculate the minimum and maximum predicted prices
min_price = min(predictions[:, 1])
max_price = max(predictions[:, 0])

# Print the predicted price range
print(f"The predicted price range for the next two weeks is ${min_price:.2f} to ${max_price:.2f}")
