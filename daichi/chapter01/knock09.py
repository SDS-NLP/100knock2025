import random

def typoglycemia(sentence):
    words = sentence.split()  # 単語に分割
    result = []

    for word in words:
        if len(word) <= 4:
            result.append(word)
        else:
            head = word[0]
            tail = word[-1]
            middle = list(word[1:-1])

            random.shuffle(middle)  # 中身をランダムに並び替え
            shuffled = head + ''.join(middle) + tail
            result.append(shuffled)

    return ' '.join(result)


text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(text))
