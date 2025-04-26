t1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

t1 = t1.replace(",", "").replace(".", "")

words = t1.split()

lengths = []

for word in words:
    length = len(word)
    lengths.append(length)

print(lengths)
