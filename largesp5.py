import pandas as pd


nyse = nyse.set_index("Stock Symbol")
nyse["Market Capitalization"].idmax()
