# 文章textにおいて、2つの名詞が「の」で連結されている名詞句をすべて抽出せよ。
import MeCab

mecab = MeCab.Tagger('-Ochasen')

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

node = mecab.parseToNode(text)

while node:
    if node.feature.split(',')[0] == '名詞':
        word = node.surface
        if node.next.surface == 'の' and node.next.next.feature.split(',')[0] == '名詞':
            print(word + node.next.surface + node.next.next.surface)
    node = node.next

