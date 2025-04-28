import pandas as pd

df = pd.read_table('iori/chapter02/popular-names.txt', header=None)

print(df.shape[0])

#wc -l iori/chapter02/popular-names.txt
#2780