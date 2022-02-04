from datetime import date
import numpy as np
import pandas as pd
import yfinance as yf
from pylab import mpl, plt
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

grp_tickers = ['MSFT', 'AAPL', 'FB', 'ADBE']
data = yf.download(grp_tickers, start='2020-01-01')
data = data['Close']


comp = yf.Ticker("MSFT")
comp = comp.info
print(comp)
