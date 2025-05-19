
from collections import Counter

# まず1列目だけ取り出してリストにする
names = []
with open('./daichi/chapter02/popular-names.txt') as f:
    for line in f:
        name = line.split('\t')[0]  # タブ区切りの1列目を取得
        names.append(name)

# 出現回数をカウント
counter = Counter(names)

# 出現回数の多い順に並べて出力
for name, count in counter.most_common():
    print(f"{name}\t{count}")
