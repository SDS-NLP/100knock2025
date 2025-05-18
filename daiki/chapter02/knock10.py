file = "daiki/chapter02/popular-names.txt"

with open(file, 'r') as r:
    #'r'は読み込みモードという意味
    count = 0
    for line in r:
        count += 1
print(count)

#wcコマンド: wc -l daiki/chapter02/popular-names.txt
#結果：2780
#-lはlineの略で行数を数える時に使う。