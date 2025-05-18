# 2つの文字列「パトカー」と「タクシー」の文字を先頭から交互に連結し、文字列「パタトクカシーー」を得よ。

text1 = 'パトカー'
text2 = 'タクシー'

result_text = ''

for t1, t2 in zip(text1, text2):
    result_text += t1 + t2

print(result_text)
