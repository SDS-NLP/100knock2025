import pandas as pd

df = pd.read_table('iori/chapter02/popular-names.txt', header=None)

n = 2
idx = df.shape[0] // n
for i in range(n):
    df_split = df.iloc[i * idx:(i + 1) * idx]
    df_split.to_csv(f"iori/chapter02/popular-names{i}.txt", sep="\t",header=False, index=False)

#split -n 2 iori/chapter02/popular-names.txt

#結果は省略