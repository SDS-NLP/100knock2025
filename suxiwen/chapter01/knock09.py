def typoglycemia(word):
    if len(word) <= 4:
        return word
    chars = list(word)
    first = chars[0]
    last = chars[-1]
    middle = chars[1:-1]
    random.shuffle(middle)
    return first + ''.join(middle) + last

sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = sentence.split()
processed_words = [typoglycemia(word) for word in words]
result = ' '.join(processed_words)

print("元の文：")
print(sentence)
print("\n処理後の文：")
print(result)