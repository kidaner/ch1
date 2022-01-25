import yfinance as yf
import yahoo_fin.stock_info as si
import pandas as pd
msft_data = si.get_quote_table("MSFT")
# print(msft_data)

comp = yf.Ticker("MSFT")
dict = comp.info
df = pd.DataFrame.from_dict(dict, orient='index')
df = df.reset_index()


stats = ["Share Price", "200D Avg Price", "Avg Target Price", "Market Cap", "Enterprise Value", "Cash", "Debt", "EBITDA Margin",
         "Revenue Growth", "Debt/Equity", "EV/Sales", "EV/EBITDA", "Price/Earnings"]
numbers = [dict["currentPrice"], dict["twoHundredDayAverage"], dict["targetMeanPrice"], dict["marketCap"],
           dict["enterpriseValue"], dict["totalCash"], dict["totalDebt"], dict["ebitdaMargins"], dict["revenueGrowth"],
           dict["debtToEquity"], dict["enterpriseToRevenue"], dict["enterpriseToEbitda"], dict["forwardPE"]]

company = pd.DataFrame(numbers, columns=["MSFT"], index=stats)
print(company)
