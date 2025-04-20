sentence: str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ans: list[int] = []

words: list[str] = sentence.split(" ")

for word in words:
    ans.append(len(word))

print(ans)