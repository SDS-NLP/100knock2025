#1列目の文字列の異なり(文字列の種類)を求めよ

#set():自動で重複を排除してくれる
first_columns=set()
filename="mao/chapter02/popular-names.txt"

with open(filename,"r") as f:
    for line in f:
        first_column=line.rstrip().split("\t")[0] 
        first_columns.add(first_column)

for value in first_columns:
    print(value)

#UNIXコマンド
#cut -f 1 mao/chapter02/popular-names.txt | sort | uniq 