from pandas_datareader.data import DataReader
from datetime import date

import pyEX as p

c = p.Client(api_token)
start = date(2015, 1, 1)
end = date(2016, 12, 31)

ticker = "GOOG"
data_source = "google"

stock_data = DataReader(ticker, data_source, start, end)
