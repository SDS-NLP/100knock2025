
# ファイルを読み込んで、行ごとにリストにする
with open('./daichi/chapter02/popular-names.txt') as f:
    lines = f.readlines()

# ソート（keyに「3列目の値」を指定、降順）
lines_sorted = sorted(lines, key=lambda x: int(x.split('\t')[2]), reverse=True)

# 出力
for line in lines_sorted:
    print(line.rstrip())
