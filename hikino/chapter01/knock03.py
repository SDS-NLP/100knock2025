sen = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
result = sen.split(" ")
len_list = []
for i in range(len(result)):
  len_list.append(len(result[i]))
print(len_list)