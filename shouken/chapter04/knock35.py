import CaboCha

sentence = "メロスは激怒した。"
c = CaboCha.Parser()
tree = c.parse(sentence)
print(tree.toString(CaboCha.FORMAT_TREE)) 
