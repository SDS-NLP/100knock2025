import CaboCha

# CaboChaパーサの初期化
parser = CaboCha.Parser()

# 対象文
sentence = "太郎はこの本を二郎を見た女性に渡した。"

# 構文解析
tree = parser.parse(sentence)

# 構文木形式（ツリー構造）で表示
print(tree.toString(CaboCha.FORMAT_TREE))
