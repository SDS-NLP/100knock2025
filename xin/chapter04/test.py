import MeCab

# 出力形式を「chasen」に、辞書をIPA辞書に明示指定
tagger = MeCab.Tagger()

text = "私は東京に住んでいますa。"
print(tagger.parse(text))
parsed = tagger.parse(text)
for line in parsed.splitlines():
    if line == 'EOS':
        continue
    parts = line.split('\t')
    if len(parts) < 2:
        continue
    surf= parts[0]
    feats =parts[4].split('-')
    print(surf, feats)