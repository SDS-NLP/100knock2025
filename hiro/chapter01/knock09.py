import random

def shuffle_inner_chars(sentence: str) -> list[str]:
    words = sentence.split(' ')
    shuffled_words = []
    for word in words:
        if len(word) > 4:
            middle_chars = list(word[1:-1])
            random.shuffle(middle_chars)
            shuffled_word = word[0] + "".join(middle_chars) + word[-1]
            shuffled_words.append(shuffled_word)
        else:
            shuffled_words.append(word)
    return ' '.join(shuffled_words)

input_sentence: str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
shuffled_sentence = shuffle_inner_chars(input_sentence)
print(f"原文　: {input_sentence}")
print(f"混合文: {shuffled_sentence}")