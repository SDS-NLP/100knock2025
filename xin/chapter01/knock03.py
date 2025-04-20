sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = [word.strip(",.") for word in sentence.split()]
word_lengths = [len(word) for word in words]
print(word_lengths)