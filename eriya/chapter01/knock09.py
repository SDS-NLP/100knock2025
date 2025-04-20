import random

def shuffle_word(word):
    if len(word) > 4:
        # 単語の先頭と末尾を残し、その中間部分をランダムに並べ替える
        middle = word[1:-1]
        shuffled_middle = list(middle)
        random.shuffle(shuffled_middle)
        return word[0] + ''.join(shuffled_middle) + word[-1]
    else:
        # 長さが4以下の単語はそのまま
        return word

def shuffle_sentence(sentence):
    words = sentence.split()  # 文を単語に分割
    shuffled_words = [shuffle_word(word) for word in words]
    return ' '.join(shuffled_words)

# テスト用の文
sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

# 実行結果
shuffled = shuffle_sentence(sentence)
print("元の文:", sentence)
print("並び替え後:", shuffled)
