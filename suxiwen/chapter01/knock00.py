s1 = "パトカー"
s2 = "タクシー"


result = ""
for c1, c2 in zip(s1, s2):
    result += c1 + c2

print(result)  