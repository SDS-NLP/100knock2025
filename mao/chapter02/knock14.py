#ファイルの先頭10行に対して各行の１列目だけを出力
N=10
filename="mao/chapter02/popular-names.txt"
with open(filename,"r") as f:
    for _ in range(N):
        line=f.readline()
        if not line:
            break
        #rstrip():行末の改行を消して綺麗にする
        first_line=line.rstrip().split("\t")[0]
        print(first_line)

#UNIXコマンド
#cut -f 1:タブ区切りの１列目だけを取り出す
#head -n 10 mao/chapter02/popular-names.txt | cut -f 1