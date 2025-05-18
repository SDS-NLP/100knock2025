#14.一列目を出力

path="popular-names.txt"

n=10
with open(path, "r", encoding="utf-8") as f:
    for i,line in enumerate(f):
        if i >= n:
            break
        category=line.strip().split("\t")
        print(category[0])

### unixコマンド ###
# head -n 10 popular-names.txt | cut -f 1

### 実行結果 ###
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