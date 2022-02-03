import yfinance as yf
import matplotlib.pyplot as plt

data = yf.Ticker('TSLA')
price = data.history(period='1y')

x = price['Close'].pct_change()

# x.plot(kind='hist')
x.plot()

plt.savefig('plot.png')
