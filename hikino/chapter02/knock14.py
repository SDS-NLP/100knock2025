import pandas as pd
df = pd.read_csv("../../../popular-names.txt", sep="\t", header = None)
df = df.loc[:10][0]
print(df)

#head -n 10 ../../../popular-names.txt | cut -f 1
#実行結果
# Mary
# Anna
# Emma
# Elizabeth
# Minnie
# Margaret
# Ida
# Alice
# Bertha
# Sarah