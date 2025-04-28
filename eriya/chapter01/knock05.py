# n-gram を生成する関数
def ngram(sequence, n):
    return [sequence[i:i+n] for i in range(len(sequence)-n+1)]

# 対象の文
text = "I am an NLPer"

# 文字 tri-gram
char_trigram = ngram(text.replace(" ", ""), 3)
print("Character tri-gram:", char_trigram)

# 単語 bi-gram
word_bigram = ngram(text.split(), 2)
print("Word bi-gram:", word_bigram)
