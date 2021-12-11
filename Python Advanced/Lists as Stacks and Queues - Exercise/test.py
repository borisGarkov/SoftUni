import pandas as pd
import yfinance as yf

trailingPEs = {
    "key": 2,
    "check": 6
}

# payload = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
# first_table = payload[0]
#
# df = first_table
#
# symbols = df['Symbol'].values.tolist()
#
# for s in symbols:
#     current_symbol = yf.Ticker(s)
#     try:
#         pe = current_symbol.info["trailingPE"]
#     except:
#         pe = 0
#
#     if s not in trailingPEs:
#         trailingPEs[s] = pe

trailingPEs = dict(sorted(trailingPEs.items(), key=lambda x: -x[1]))
for key, value in trailingPEs.items():
    print(f"{key} - {value}")
