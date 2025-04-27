N = 10
file = "/Users/aa/Downloads/popular-names.txt"
with open(file, "r") as r:
    lines = r.readlines()#すべての行をリストとして読み込む
    lines.reverse()
    for i in range(N):
        print(lines[i], end = "")
#unixコマンド　tail -n 10 (ファイル)