text="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words=text.split()


for i in range(len(words)):
    words[i]=len(words[i].strip(",."))

print(words)
