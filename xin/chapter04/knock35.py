import CaboCha
import pydot

text = "メロスは激怒した。"

# CaboChaの初期化
parser = CaboCha.Parser()
tree = parser.parse(text)

# グラフの初期化
graph = pydot.Dot(graph_type="digraph", charset="utf-8")

# 係り受け関係を取得
chunks = []
for i in range(tree.chunk_size()):
    chunk = tree.chunk(i)
    surface = "".join(tree.token(j).surface for j in range(chunk.token_pos, chunk.token_pos + chunk.token_size))
    chunks.append(surface)

for i in range(tree.chunk_size()):
    chunk = tree.chunk(i)
    if chunk.link != -1:  # 係り先がある場合のみ
        src_surface = chunks[i]  # 係り元の文節
        dst_surface = chunks[chunk.link]  # インデックスではなく、対応するテキスト
        edge = pydot.Edge(src_surface, dst_surface,fontname="Noto Sans CJK JP", fontsize="12", color="black")
        graph.add_edge(edge)
# 画像として保存
graph.write_png("dependency_tree.png")
print("係り受け木を 'dependency_tree.png' に保存しました。")