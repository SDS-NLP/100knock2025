import random

def shuffle_inner(word):
    """単語の先頭と末尾を維持し、内部の文字をランダムに並び替える"""
    if len(word) <= 4:
        return word  # 長さが4以下ならそのまま返す
    inner_chars = list(word[1:-1])
    random.shuffle(inner_chars)
    return word[0] + "".join(inner_chars) + word[-1]

def process_sentence(sentence):
    """文章内の単語を変換"""
    words = sentence.split()
    return " ".join(shuffle_inner(word) for word in words)

# 実行例
sentence = "Often considered to be the first modern novel, Don Quixote is a wonderful burlesque of the popular literature its disordered protagonist is obsessed with."
result = process_sentence(sentence)
print(result)