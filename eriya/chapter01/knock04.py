sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# ピリオドを削除
sentence = sentence.replace('.', '')
words = sentence.split()

# 指定された単語の位置（1始まり）
one_letter_indices = {1, 5, 6, 7, 8, 9, 15, 16, 19}

# 結果の辞書
element_dict = {}

for i, word in enumerate(words, 1):
    if i in one_letter_indices:
        key = word[:1]
    else:
        key = word[:2]
    element_dict[key] = i

# 出力
print(element_dict)
