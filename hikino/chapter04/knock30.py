import MeCab

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

tagger = MeCab.Tagger("-Owakati -r /etc/mecabrc")
node = tagger.parseToNode(text)

dct= {}

while node:
  word = node.surface
  pos = node.feature.split(",")[0]
  tpl = (word, pos)
  if word != "":
    dct[f"{word}"] = pos
  node = node.next

keys = [k for k, v in dct.items() if v == '動詞']
print(keys)