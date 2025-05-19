# 「メロスは激怒した。」の係り受け木を可視化せよ。

import CaboCha

text = "メロスは激怒した。"

parser = CaboCha.Parser()
tree = parser.parseToString(text)

print(tree)
