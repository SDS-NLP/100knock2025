import MeCab
import ipadic

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

mecab = MeCab.Tagger(ipadic.MECAB_ARGS)
parsed_text = mecab.parse(text)

verbs = []
for line in parsed_text.splitlines():
    if line == "EOS" or line == "":
        continue
    parts = line.split("\t")
    if len(parts) > 1:
        features = parts[1].split(",")
        if features[0] == "動詞":
            verbs.append(parts[0])

print(verbs)