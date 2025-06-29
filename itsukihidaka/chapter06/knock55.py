import pandas as pd

df = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter06/knock54.csv')

accuracy = 0
for i in range(len(df)):
  if df.iloc[i]['word4'] == df.iloc[i]['similar_word']:
    accuracy += 1

print(accuracy/len(df))


