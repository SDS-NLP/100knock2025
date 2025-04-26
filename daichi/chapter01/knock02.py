#文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ。

#多分一番簡単
a = "stressed"
print(a[::-1])

#for文を使って書いてみる
result = ""
for i in range(len(a)):
    result += a[len(a)-i-1]
print(result)

#Whileつかってみる
b = 0
result1 = ""
while b < len(a):
    result1 += a[-1 - b]
    b += 1
print(result1)