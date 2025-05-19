
unique_names = set()

with open('./daichi/chapter02/popular-names.txt') as f:
    for line in f:
        name = line.split('\t')[0]  # 1列目だけ取り出す（タブで区切られている）
        unique_names.add(name)      # 集合に追加（重複は自動で無視される）

# 結果を表示（並び替えたいなら sorted() を使う）
for name in sorted(unique_names):
    print(name)
