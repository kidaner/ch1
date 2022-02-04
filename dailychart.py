import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = input("Please enter ticker: ")

company = yf.Ticker(ticker)

trailingEps = company.info["trailingEps"]
forwardEps = company.info["forwardEps"]

price = company.history(period='1y')
price = price["Close"]

price_earnings = price / trailingEps
plt.plot(price, price_earnings)
plt.show()
