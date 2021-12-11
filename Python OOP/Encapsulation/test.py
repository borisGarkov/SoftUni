import pandas as pd

df = pd.read_csv('pokemon_data.csv')
# print(df.sort_values("Name"))
# df["Total"] = df["HP"] + df["Attack"]
print(df.head(5))
print(df.loc[:, ["Name"]])
