import MeCab

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

tagger = MeCab.Tagger()
sentences = []
morphs = []

for line in tagger.parse(text).splitlines():
    if line == 'EOS':
        if morphs:
            sentences.append(morphs)
            morphs = []
        continue

    if '\t' not in line:
        continue

    surface, feature_str = line.split('\t', maxsplit=1)
    feature = feature_str.split(',')

    if len(feature) < 7:
        continue

    morph = {
        'surface': surface,
        'base': feature[6],
        'pos': feature[0],
        'pos1': feature[1]
    }

    morphs.append(morph)

for i, sentence in enumerate(sentences):
    print(f'--- 文{i+1} ---')
    for m in sentence:
        print(m)
