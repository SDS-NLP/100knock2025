from janome.tokenizer import Tokenizer

text = """メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

# 形態素解析器の初期化
tokenizer = Tokenizer()

# 文章を解析
tokens = tokenizer.tokenize(text)

# 動詞を抽出
verbs = []
for token in tokens:
    part=token.part_of_speech.split(",")[0]
    if part == "動詞":
        verbs.append(token.surface)

# 結果の表示
for verb in verbs:
    print(verb)