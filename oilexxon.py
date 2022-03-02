import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import yfinance as yf

tickers = input("Ticker(s): ")
start = "2021-12-31"
end = "2022-3-1"

# company = yf.Ticker(ticker).history(period="1mo")["Close"]

both = yf.download(tickers, start=start, end=end)

data = "${:.2f}".format(both)

print(data)
