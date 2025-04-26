a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
a = a.replace(".","")

b = a.split()
c = {1,5,6,7,8,9,15,16,19}

periodic_table = {}

for i in range(len(b)):
    if i + 1 in c:
        key = b[i][:1]
    else:
        key = b[i][:2]
    periodic_table[key] = i + 1  # 1始まりの番号にする

print(periodic_table)

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = sentence.split()  # 単語に分割

# 1文字を取り出す位置（1始まり）
one_char_positions = [1, 5, 6, 7, 8, 9, 15, 16, 19]

# 結果を入れる辞書
element_dict = {}

i = 0
while i < len(words):
    word = words[i]
    word = word.strip(".")  # ピリオドを消す

    position = i + 1  # 1始まりの位置に直す

    if position in one_char_positions:
        symbol = word[0]
    else:
        symbol = word[0] + word[1]

    element_dict[symbol] = position
    i = i + 1

print(element_dict)
