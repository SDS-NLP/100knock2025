#31. 動詞の原型

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

import MeCab

# MeCab Taggerオブジェクトを作成
tagger = MeCab.Tagger()
# 解析
node = tagger.parseToNode(text)

# 動詞を抽出して表示
while node:
    features = node.feature.split(',')
    #print(features)
    # 品詞が「動詞」のものを抽出
    if features[0] == '動詞':
        print("含まれている動詞：", node.surface, "その原型：", features[7])
    node = node.next

