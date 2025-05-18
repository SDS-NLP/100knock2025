#16.ランダムに各行を並び替える
import pandas as pd

path="popular-names.txt"
df = pd.read_csv(path, header=None, sep="\t", encoding="utf-8")
print(df.sample(frac=1))

### unixコマンド ###
# shuf popular-names.txt

### 実行結果 ###
# Minnie  F       2178    1885
# Olivia  F       19807   2014
# Edward  M       2125    1887
# Christopher     M       19630   2004
# Ashley  F       17997   2000
# Andrew  M       23641   2000
# Jayden  M       16127   2012
# Andrew  M       26009   1994
# Andrew  M       22019   2002
# Mary    F       63508   1929
# Charles M       3213    1903
# Thomas  M       44572   1957
# Carol   F       30456   1944
# ...つづく
