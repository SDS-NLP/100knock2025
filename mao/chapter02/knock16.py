#ファイルを行単位でランダムに並べ替える(各行の内容は変更しない)
import random 
filename="mao/chapter02/popular-names.txt"

with open(filename,"r") as f:
    lines=f.readlines()
#random.shuffleはリストをインプレースで並び替えるので戻り値を変数にするの不要
#shuffle_lines=random.shuffle(lines)
random.shuffle(lines)
for line in lines:
    print(line)

#UNIXコマンド
#shufコマンドはファイルの内容を変更しない
#shuf mao/chapter02/popular-names.txt