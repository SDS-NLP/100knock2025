#各行の１列目の文字列の出現頻度を求め、出現頻度と名前を出現頻度の多い順に並べて表示せよ
from collections import Counter

first_columns=[] #１列目を格納するリスト（重複あり）
filename="mao/chapter02/popular-names.txt"
with open(filename,"r") as f:
    for line in f:
        first_column=line.rstrip().split("\t")[0]
        first_columns.append(first_column)

#出現頻度をカウント
#countedは辞書に似たような構造を持つ、キーが要素、値が出現回数
counted=Counter(first_columns)

#出現頻度を高い順に並べる
sorted_counts=counted.most_common()

#結果表示
for value,count in sorted_counts:
    print(f"{value}:{count}")

#UNIXコマンド
#cut -f:出力する列指定、-d:区切り文字、
#uniq -c:各行の出現回数も一緒に表示する(デフォでは重複消去)
#uniqを効率的に作用させるためには先にsortコマンドで重複させるものを連続させておくといい
#cut -f 1 mao/chapter02/popular-names.txt | sort | uniq -c |sort -nr





#UNIXコマンド
#