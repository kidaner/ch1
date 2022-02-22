import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

ticker = input("Please enter ticker: ")

company = yf.Ticker(ticker)

trailingEps = company.info["trailingEps"]
forwardEps = company.info["forwardEps"]

price = company.history(period='1y')
price = price["Close"]

price_earnings = price / trailingEps

fig, ax1 = plt.subplots()
ax1.plot(price, linewidth=3)
ax1.set_title(f"{ticker} Valuation", fontsize=14)
ax1.set_xlabel("Date", fontsize=14)
myFmt = mdates.DateFormatter('%m')
ax1.xaxis.set_major_formatter(myFmt)
fig.autofmt_xdate()
ax1.set_ylabel("Price ($)", fontsize=14)
ax1.tick_params(axis="both", labelsize=14)

ax2 = ax1.twinx()
ax2.plot(price_earnings, linewidth=3)
ax2.set_ylabel("Price/Earnings (x)", fontsize=14)

plt.show()
