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

lst= []

while node:
  word = node.surface
  pos = node.feature.split(",")[0]
  tpl = (word, pos)
  if word != "":
    lst.append(tpl)
  node = node.next

for i in range(len(lst)):
  if lst[i][1] == "助詞" and lst[i][0] == "の":
    A_noun = lst[i-1][0]
    no = lst[i][0]
    B_noun = lst[i+1][0]
    print(A_noun + no + B_noun)