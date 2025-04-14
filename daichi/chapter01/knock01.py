#一個ずつ追加してプリントする
str = "パタトクカシーー"
result = ""
result += str[1]
result += str[3]
result += str[5]
result += str[7]
print(result)

#for文を使って上の作業をやる。これならもっと長くても楽。
result1 = ""
for i in range(len(str)):
    if i % 2 != 0:
        result1 += str[i]
print(result1)

result2 = ""
num = 1
while len(result2) < len(str)/2:
    result2 += str[num]
    num += 2
print(result2)

#1つおきに取り出してプリントする。一個上のやり方よりももっと楽
print(str[1::2])  
