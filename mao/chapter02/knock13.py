#先頭10行に対してタブをスペースに変換する
N=10
filename="mao/chapter02/popular-names.txt"

with open(filename,"r") as f:
    for _ in range(N):
        line=f.readline()
        if not line:
            break
        print(line.replace("\t"," "))

#UNIXコマンド
#head -n 10 mao/chapter02/popular-names.txt | tr "\t" " "
