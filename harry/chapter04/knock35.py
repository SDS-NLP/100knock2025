import CaboCha

# CaboChaパーサの初期化
parser = CaboCha.Parser()

# 対象文
sentence = "太郎は花子に次郎の描いた絵を送った。"

# 構文解析
tree = parser.parse(sentence)

# 構文木形式（ツリー構造）で表示
print(tree.toString(CaboCha.FORMAT_TREE))
