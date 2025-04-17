str1 = "パトカー"
str2 = "タクシー"
result = "".join("".join(pair) for pair in zip(str1, str2))
print(result)
