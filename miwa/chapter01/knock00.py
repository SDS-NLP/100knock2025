str1="パトカー"
str2="タクシー"
str3=""
i=0
j=0
while i < len(str1) and j < len(str2):
    str3 = str3 + str1[i] + str2[j]
    i+=1
    j+=1

print(str3)

