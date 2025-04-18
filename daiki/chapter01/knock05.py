def n_gram(n, text):
    words = text.split()
    result = []
    for i in range(len(words) - n + 1):
        ngram = words[i:i+n]
        result.append(ngram)
    return result

trigram = n_gram(3, "I am an NLPer")
bigram = n_gram(2, "I am an NLPer")

print(trigram)
print(bigram)
