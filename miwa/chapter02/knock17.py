#17.一列目の文字列の異なり
import pandas as pd

path="popular-names.txt"
df = pd.read_csv(path, header=None, sep="\t", encoding="utf-8")

print(df[0].unique())

### unixコマンド ###
# cut -f 1 popular-names.txt| sort | uniq

### 実行結果 ###
# Abigail
# Aiden
# Alexander
# Alexis
# Alice
# Amanda
# Amelia
# Amy ...