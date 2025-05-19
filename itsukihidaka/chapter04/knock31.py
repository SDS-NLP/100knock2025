# 文章textに含まれる動詞と、その原型をすべて表示せよ。
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
    if node.feature.split(',')[0] == '動詞':
        print(f'元：{node.surface}', f'原型：{node.feature.split(",")[6]}')
    node = node.next