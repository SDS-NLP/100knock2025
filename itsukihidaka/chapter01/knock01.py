# 文字列「パタトクカシーー」の2, 4, 6, 8文字目を取り出し、それらを連結した文字列を得よ。

text = "パタトクカシーー"

result_text = ''

for i in range(0, len(text), 2):
    result_text += text[i]

print(result_text)