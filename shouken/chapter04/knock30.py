import MeCab

with open("merosu.txt", encoding="utf-8") as file:
    text = file.read()

#MeCabの解析器
tagger = MeCab.Tagger("-d /var/lib/mecab/dic/debian")

#文章を形態素に分解する
node = tagger.parseToNode(text)

#動詞だけを抽出して表示する
while node is not None:
    word = node.surface
    pos = node.feature.split(",")[0]

    if pos == "動詞":
        print(word)

    node = node.next 
