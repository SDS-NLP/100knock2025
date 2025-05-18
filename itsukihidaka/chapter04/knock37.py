# コーパスにおける名詞の出現頻度を求め、出現頻度の高い20語とその出現頻度を表示せよ。
from knock36 import texts

import MeCab

mecab = MeCab.Tagger('-Ochasen')

numcount = {}

for text in texts:
    node = mecab.parseToNode(text)
    while node:
        if node.feature.split(',')[0] == '名詞':
            if node.surface not in numcount:
                numcount[node.surface] = 0
            numcount[node.surface] += 1
        node = node.next

# 出現頻度の高い上位20語とその出現頻度を表示
for i, (word, count) in enumerate(sorted(numcount.items(), key=lambda x: x[1], reverse=True)):
    if i >= 20:
        break
    print(f"{i+1}位 単語：{word} 出現頻度：{count}")

