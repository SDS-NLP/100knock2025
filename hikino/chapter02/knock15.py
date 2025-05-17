import pandas as pd
df = pd.read_csv("../../../popular-names.txt", sep="\t", header = None)
n = int(input())
sp_n = len(df)/n
for i in range(n):
  df_n = df.loc[sp_n*i : sp_n*(i+1)-1]
  df_n.to_csv(f"../../../popular-names_split{i+1}.csv", index=False, header=False)

#split -n 10 ../../../popular-names.txt popular-names_split.txt
#実行結果
# popular-names_split.txtaa
# popular-names_split.txtab
# popular-names_split.txtac
# popular-names_split.txtad
# popular-names_split.txtae
# popular-names_split.txtaf
# popular-names_split.txtag
# popular-names_split.txtah
# popular-names_split.txtai
# popular-names_split.txtaj

