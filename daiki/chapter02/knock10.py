file = "/Users/aa/Downloads/popular-names.txt"

with open(file, 'r') as r:
    #'r'は読み込みモードという意味
    count = 0
    for line in r:
        count += 1
print(count)

#wcコマンド: wc -l /Users/aa/Downloads/popular-names.txt
#-lはlineの略で行数を数える時に使う。