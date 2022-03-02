import pandas_datareader as data
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

source = "yahoo"
start = date(2021, 12, 31)
exxon = data.DataReader("XOM", source, start)
oil = data.DataReader("CL=F", source, start)

chart = pd.concat([exxon["Close"], oil["Close"]])

print(oil)
