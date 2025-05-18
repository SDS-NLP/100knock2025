import pandas as pd

# TSVファイルの読み込み
df1 = pd.read_csv("../../../SST-2/dev.tsv", sep="\t")
df2 = pd.read_csv("../../../SST-2/train.tsv", sep="\t")

# 表示
print(df1.head())

print(df1["label"].value_counts())
print(df2["label"].value_counts())
