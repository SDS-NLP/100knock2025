# 元の文
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# 句読点を除去
cleaned_text = text.replace(",", "").replace(".", "")

# 単語に分解
words = cleaned_text.split()

# 各単語の文字数をリスト化
lengths = [len(word) for word in words]

# 出力
print(lengths)
