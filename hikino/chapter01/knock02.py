str1 = "stressed"
result = ""
for i in range(len(str1)):
  rev = len(str1) - i - 1
  result = result + str1[rev]
print(result)