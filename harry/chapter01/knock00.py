str1 = "パトカー"
str2 = "タクシー"

result = ''
for i in range(len(str1)):
    result += str1[i] + str2[i]

print(result)

# 文字列を定義
str1 = "パトカー"
str2 = "タクシー"

# zipで交互に取り出して連結
result = ''.join(a + b for a, b in zip(str1, str2))

# 結果を表示
print(result)