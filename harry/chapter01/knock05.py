def n_gram(sequence, n):
    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]

# 文字tri-gram（スペースも含む）
text = "I am an NLPer"
char_trigrams = n_gram(text, 3)
print("文字トリグラム:", char_trigrams)

# 単語bi-gram
words = text.split()
word_bigrams = n_gram(words, 2)
print("単語バイグラム:", word_bigrams)
