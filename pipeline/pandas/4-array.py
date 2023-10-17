import pandas as pd

df = from_file('../supervised_learning/data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
A = df.loc[:, ['High', 'Close']].tail(10).to_numpy()

print(A)
