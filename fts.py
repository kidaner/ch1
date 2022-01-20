from re import T
import numpy as np
import pandas as pd
import yfinance as yf
from pylab import mpl, plt
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

grp_tickers = ['MSFT', 'AAPL', 'FB', 'ADBE']

for t in grp_tickers:
    ticker = yf.Ticker(t)
    history = ticker.history(period='5d')
    data = pd.DataFrame(
        history['Close'], index=history[0], columns=grp_tickers)
    data = pd.concat(data, history['Close'], how='left')
print(data)
