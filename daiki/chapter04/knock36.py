import MeCab
from collections import Counter

# ファイルを読み込み
with open("daiki/chapter04/kokoro.txt", "r", encoding="utf-8") as f:
    text = f.read()

# MeCabで形態素解析
tagger = MeCab.Tagger()
node = tagger.parseToNode(text)

# 単語（名詞や動詞など）の表層形を集める
words = []
while node:
    surface = node.surface
    features = node.feature.split(",")
    # 「記号」などを除外したい場合は、名詞・動詞・形容詞などで絞れる
    if features[0] != "記号" and surface != "":
        words.append(surface)
    node = node.next

# 頻度をカウント
counter = Counter(words)

# 上位20語を表示
print("出現頻度上位20語:")
for word, freq in counter.most_common(20):
    print(f"{word}\t{freq}")
