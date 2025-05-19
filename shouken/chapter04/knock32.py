import MeCab

with open("merosu.txt", encoding="utf-8") as file:
    text = file.read()

tagger = MeCab.Tagger("-d /var/lib/mecab/dic/debian")

node = tagger.parseToNode(text)

history = []

while node is not None:
    surface = node.surface
    pos = node.feature.split(",")[0]

    # 直近3つの (単語, 品詞) を記録
    history.append((surface, pos))

    # 3語たまったら「名詞＋の＋名詞」パターンをチェック
    if len(history) == 3:
        word1, pos1 = history[0]
        word2, pos2 = history[1]
        word3, pos3 = history[2]

        if pos1 == "名詞" and word2 == "の" and pos2 == "助詞" and pos3 == "名詞":
            print(word1 + word2 + word3)

        # 一番古い単語を削除して、次の組を探す準備
        history.pop(0)

    node = node.next  # 次の単語へ
