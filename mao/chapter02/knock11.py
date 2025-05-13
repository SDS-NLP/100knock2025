#ファイルの先頭N行だけを表示せよ
N=10
filename="mao/chapter02/popular-names.txt"
with open(filename,"r") as f:
    for i in range(N):
        line=f.readline()
        if not line: #ファイルがN行未満なら終了する
            break
        print(line)

#UNIXコマンド
#head -n 10 mao/chapter02/popular-names.txt