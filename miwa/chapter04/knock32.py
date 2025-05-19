#32. 「AのB」
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

# 結果を入れる
result = []

while node:
    # ３つ連続の形態素を取得して判定するので、次の２つノードも取得
    node1 = node
    node2 = node1.next
    node3 = node2.next if node2 else None

    if node3:
        f1 = node1.feature.split(',')
        f2 = node2.feature.split(',')
        f3 = node3.feature.split(',')

        # 条件：名詞 + の（助詞） + 名詞
        if (f1[0] == '名詞' and
            node2.surface == 'の' and f2[0] == '助詞' and
            f3[0] == '名詞'):
            phrase = node1.surface + node2.surface + node3.surface
            result.append(phrase)

    node = node.next

print("名詞句（AのB）一覧:")
for phrase in result:
    print(phrase)
