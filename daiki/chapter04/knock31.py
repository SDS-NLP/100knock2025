import MeCab

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""
#MeCab の解析器（Tagger）を作成
tagger = MeCab.Tagger()

verbs = []
verb_bases = []

#各行に対して解析
node = tagger.parseToNode(text)#「メロスは激怒した」→「メロス」「は」「激怒」「し」「た」に分解

while node:
    features = node.feature.split(',')#node.feature にはその単語の解析情報（カンマ区切りの文字列）が入っているのでリスト化する
    if features[0] == '動詞':#features[0]は品詞情報
        surface = node.surface#surfaceは表層系 ex)「走った」の場合 → surface = 「走っ」
        base = features[6]#features[6]はその単語の原型 ex)走った」の原型 → 「走る」
        verbs.append(surface)
        verb_bases.append(base)
        node = node.next#ループを回す
print(verbs)
print(verb_bases)