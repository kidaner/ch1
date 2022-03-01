from pandas_datareader import DataReader
import pandas as pd
from datetime import date
import pyEX as p
import os
import matplotlib.pyplot as plt

os.environ["IEX_API_KEY"] = "pk_b66ca6ae85d64d62a07e050601d1bcc7"

start = date(2010, 1, 1)
series = "DCOILWTICO"
oil = DataReader(series, "fred", start)

ticker = "XOM"
stock = DataReader(ticker, "iex", start)

data = pd.concat([stock["close"], oil], axis=2)

data.columns = ["Exxon", "Oil Price"]

data.plot()

plt.show()
