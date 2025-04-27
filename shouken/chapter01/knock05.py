def ngram(sequence, n):
    result = []
    for i in range(len(sequence) - n + 1):
        result.append(sequence[i:i+n])
    return result

t1 = "I am an NLPer"

t2 = t1.replace(" ", "")
char_trigrams = ngram(t2, 3)
print("文字 tri-gram:")
print(char_trigrams)

words = t1.split()
word_bigrams = ngram(words, 2)
print("\n単語 bi-gram:")
print(word_bigrams)
