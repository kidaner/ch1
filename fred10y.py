from os import stat
from pandas_datareader import DataReader
from datetime import date
import matplotlib.pyplot as plt

series_code = "DGS10"
data_source = "fred"
start = date(1962, 1, 1)

data = DataReader(series_code, data_source, start)

series_name = "10-Year Treasury"
data = data.rename(columns={series_code: series_name})

data.plot()

plt.show()
