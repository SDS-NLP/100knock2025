sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# 各単語から句読点を除き、文字数をカウント
word_lengths = [len(word.strip(".,;:!?")) for word in sentence.split()]
print(word_lengths)