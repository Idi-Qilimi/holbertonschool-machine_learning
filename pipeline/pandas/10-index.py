import pandas as pd

df = from_file('../supervised_learning/data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df = df.set_index('Timestamp')

print(df.tail())
