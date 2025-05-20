import MeCab
from collections import Counter

# kokoro.txtを読み込む
with open("daiki/chapter04/kokoro.txt", "r", encoding="utf-8") as f:
    text = f.read()

# MeCabのTagger作成（unidicを使う場合は -d オプションが必要）
tagger = MeCab.Tagger()
node = tagger.parseToNode(text)

# 名詞だけを集める
nouns = []
while node:
    surface = node.surface
    features = node.feature.split(",")
    # features[0] が「名詞」のときだけ収集
    if features[0] == "名詞" and surface != "":
        nouns.append(surface)
    node = node.next

# 出現頻度を数える
counter = Counter(nouns)

# 上位20語を表示
print("出現頻度の高い名詞20語:")
for word, freq in counter.most_common(20):
    print(f"{word}\t{freq}")
