#15.ファイルをN分割する
import pandas as pd
import math

path="popular-names.txt"
n=4

df = pd.read_csv(path, header=None, sep="\t", encoding="utf-8")

lines_number=math.ceil(len(df)/n)
for i in range(n):
    start=i*lines_number
    end=start+lines_number
    block=df.iloc[start:end]

    new_path=f"popular-names_{i}.txt"
    block.to_csv(new_path,header=False,index=False)

### unixコマンド ###
# split -l $(($(wc -l < popular-names.txt) / 4)) popular-names.txt output_part_
# N=4で実行

### 実行結果 ###
# output_part_aa, output_part_ab, output_part_ac, output_part_ad が生成された
