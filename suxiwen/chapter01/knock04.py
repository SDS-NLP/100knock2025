def create_ngram(sequence, n):
    return [tuple(sequence[i:i+n]) for i in range(len(sequence) - n + 1)]

text = "I am an NLPer"


char_tri_gram = create_ngram(list(text), 3)


word_bi_gram = create_ngram(text.split(), 2)

print("文字tri-gram：", char_tri_gram)
print("単語bi-gram：", word_bi_gram)