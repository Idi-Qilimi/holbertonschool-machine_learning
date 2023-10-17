import pandas as pd

df = from_file('../supervised_learning/data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Remove the 'Weighted_Price' column
df.drop(columns=['Weighted_Price'], inplace=True)

# Fill missing values in 'Close' with the previous row's value
df['Close'].fillna(method='ffill', inplace=True)

# Fill missing values in 'High', 'Low', and 'Open' with the same row's 'Close' value
df['High'].fillna(df['Close'], inplace=True)
df['Low'].fillna(df['Close'], inplace=True)
df['Open'].fillna(df['Close'], inplace=True)

# Fill missing values in 'Volume_(BTC)' and 'Volume_(Currency)' with 0
df['Volume_(BTC)'].fillna(0, inplace=True)
df['Volume_(Currency)'].fillna(0, inplace=True)

print(df.head())
print(df.tail())
