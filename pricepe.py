import yfinance as yf
import yahoo_fin.stock_info as si
import pandas as pd
import good_morning as gm
msft_data = si.get_quote_table("MSFT")
# print(msft_data["PE Ratio (TTM)"])

microsoft = yf.Ticker("MSFT")
dict = microsoft.info
df = pd.DataFrame.from_dict(dict, orient='index')
df = df.reset_index()
print(df[6])

kr = gm.KeyRatiosDownloader()
kr_frames = kr.download("MSFT")
