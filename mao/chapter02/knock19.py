#3列目の数値の逆順でファイルの各行を整理せよ、(各行の内容を変更しない)

filename="mao/chapter02/popular-names.txt"

with open(filename,"r") as f:
    lines=f.readlines()
#key:並べ替えの基準となる値を各要素から抽出する関数
sorted_lines=sorted(lines,key=lambda x:float(x.split("\t")[2]))

for line in sorted_lines:
    print(line)

#UNIXコマンド
#sort -k3,3nr mao/chapter02/popular-names.txt