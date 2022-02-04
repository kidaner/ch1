import yfinance as yf
import yahoo_fin.stock_info as si
import pandas as pd
msft_data = si.get_quote_table("MSFT")
# print(msft_data)

comp = yf.Ticker("MSFT")
dict = comp.info
df = pd.DataFrame.from_dict(dict, orient='index')
df = df.reset_index()


stats = ["Share Price", "200D Avg Price", "Avg Target Price", "Market Cap $b", "Enterprise Value $b", "Cash $b", "Debt $b", "EBITDA Margin",
         "Revenue Growth", "Debt/Equity", "EV/Sales", "EV/EBITDA", "Price/Earnings"]
numbers = [dict["currentPrice"], dict["twoHundredDayAverage"], dict["targetMeanPrice"], dict["marketCap"] / 1000000000,
           dict["enterpriseValue"] / 1000000000, dict["totalCash"] /
           1000000000, dict["totalDebt"] /
           1000000000, dict["ebitdaMargins"], dict["revenueGrowth"],
           dict["debtToEquity"], dict["enterpriseToRevenue"], dict["enterpriseToEbitda"], dict["forwardPE"]]

pd.set_option('display.float_format', '{:.2f}'.format)
company = pd.DataFrame(numbers, columns=["MSFT"], index=stats)

print(company)
