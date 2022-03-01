from pandas_datareader import DataReader
import pandas as pd
from datetime import date
import pyEX as p
import os
import matplotlib.pyplot as plt

start = date(1950, 1, 1)

series = ['UNRATE', 'CIVPART']

econ_data = DataReader(series, "fred", start=start)

econ_data.columns = ["Unemployment Rate", "Participation Rate"]

econ_data.plot(subplots=True, title="Labor Market")

plt.show()
