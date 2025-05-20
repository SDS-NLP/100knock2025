import MeCab

m = MeCab.Tagger("-Ochasen")
text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""
sentences = text.split('\n')
verbs = []
for sent in sentences:
    if not sent.strip():
        continue
    node = m.parseToNode(sent)
    while node:
        if node.feature.split(',')[0] == '動詞':
            verbs.append(node.surface)
        node = node.next
print(verbs)
# 実行結果: ['激怒', '除', '決意', 'わか', 'あ', '吹', '遊', '暮', '来', '敏感']