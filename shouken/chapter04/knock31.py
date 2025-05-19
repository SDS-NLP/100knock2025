import MeCab

with open("merosu.txt", encoding="utf-8") as file:
    text = file.read()

tagger = MeCab.Tagger("-d /var/lib/mecab/dic/debian")

#形態素に分解
node = tagger.parseToNode(text)

#動詞を1つずつチェック
while node is not None:
    surface = node.surface
    features = node.feature.split(",")

    # 動詞で、かつ辞書形がある場合
    if len(features) > 6 and features[0] == "動詞":
        base_form = features[6]             #辞書形
        print(f"{surface} → {base_form}")

    node = node.next
