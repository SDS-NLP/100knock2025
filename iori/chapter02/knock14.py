import pandas as pd

df = pd.read_table('iori/chapter02/popular-names.txt', header=None)

df = df.head(10)

print(df.iloc[:,0])

#head -n 10 iori/chapter02/popular-names.txt | cut -f 1
'''Mary
Anna
Emma
Elizabeth
Minnie
Margaret
Ida
Alice
Bertha
Sarah'''