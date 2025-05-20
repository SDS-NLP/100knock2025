import MeCab

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

results = []
#形態素解析して1文ずつ処理
for line in text.split('。'):
    node = mecab.parseToNode(line)
    words = []
    while node:
        surface = node.surface()
        features = node.feature.split(',')
        pos = features[0]
        words.append((surface, pos))
        node = node.next

    #「名詞 の 名詞」を検出
    for i in range(1, len(words) - 1):
        if words[i][0] == 'の':
            if words[i-1][1] == '名詞' and words[i+1][1] == '名詞':
                phrase = words[i-1][0] + words[i][0] + words[i+1][0]
                results.append(phrase)
for i in range(results):
    print(i)