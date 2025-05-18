text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word = []

text = text.replace(",", "")
text = text.replace(".", "")

for i in text.split():
    word.append(i)

ans = [len(i) for i in word]
print(ans)