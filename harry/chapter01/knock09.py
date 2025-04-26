import random
import re

def shuffle_inner(word):
    if len(word) <= 4:
        return word
    # 単語の先頭と末尾を除いた中身をシャッフル
    mid = list(word[1:-1])
    random.shuffle(mid)
    return word[0] + ''.join(mid) + word[-1]

def typoglycemia(text):
    # 単語＋記号（例: "mind." や "reading:"）を分けて処理
    words = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
    result = []
    for word in words:
        if word.isalpha():
            result.append(shuffle_inner(word))
        else:
            result.append(word)
    return ' '.join(result)

# 実行例の文
input_text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

# 出力
output_text = typoglycemia(input_text)
print("変換後：")
print(output_text)
