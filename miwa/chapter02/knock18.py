#18. 各行の1列目の文字列の出現頻度を求め、出現頻度の高い順に並べる
import pandas as pd

path="popular-names.txt"
df = pd.read_csv(path, header=None, sep="\t", encoding="utf-8")

count_series=df[0].value_counts()
for name,count in count_series.items():
    print(count,name)


### unixコマンド ###
# cut -f 1 popular-names.txt| sort | uniq -c | sort -nr

### 実行結果 ###
# 118 James
# 111 William
# 108 Robert
# 108 John
# 92 Mary
# 75 Charles
# 74 Michael
# 73 Elizabeth...