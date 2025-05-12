#19. 3列目の数値の降順に各行を並び替える
import pandas as pd

path="popular-names.txt"
df = pd.read_csv(path, header=None, sep="\t", encoding="utf-8")

sorted_by_third=df.sort_values(df.columns[2],ascending=False)
print(sorted_by_third)

### unixコマンド ###
# sort -k 3,3 -n -r popular-names.txt

### 実行結果 ###
# Linda   F       99689   1947
# Linda   F       96211   1948
# James   M       94757   1947
# Michael M       92704   1957
# Robert  M       91640   1947
# Linda   F       91016   1949
# Michael M       90656   1956
# Michael M       90517   1958
# James   M       88584   1948
# Michael M       88528   1954