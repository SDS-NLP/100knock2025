#フィイルの行数をカウントせよ、確認にはwcコマンド用いよ
filename="mao/chapter02/popular-names.txt"

with open(filename,"r") as f:
    lines=f.readlines()
    print(len(lines))  #2780

#UNIXコマンド
#wc -l mao/chapter02/popular-names.txt
