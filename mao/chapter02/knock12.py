#ファイルの末尾N行を出力
N=10
filename="mao/chapter02/popular-names.txt"

with open(filename,"r") as f:
    lines=f.readlines()
    for line in lines[-N:]:
        print(line)

#UNIXコマンド
#tail -n 10 mao/chapter02/popular-names.txt