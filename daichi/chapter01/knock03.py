a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

a = a.replace(",","").replace(".","")

b =[len(word) for word in a.split()]
print(b)

# for文を使ってやってみる
c = []
d = 0
for i in range(len(a)):
    if a[i] == " ":
        c.append(i - d)
        d = i + 1
c.append(len(a) - d)
print(c)
