sent = "メロスは激怒した。"
import graphviz
dot = graphviz.Digraph()
result = m.parse(sent)
lines = result.split('\n')
nodes = []
edges = []
for i, line in enumerate(lines):
    if line.startswith('EOS') or not line.strip():
        continue
    parts = line.split('\t')
    nodes.append(parts[0])
    if len(parts) >= 8:
        dst_idx = parts[7]
        if dst_idx != '-1':
            edges.append((i, int(dst_idx)))
for i, node in enumerate(nodes):
    dot.node(str(i), node)
for src, dst in edges:
    dot.edge(str(src), str(dst))
dot.render('dependency_tree', view=True)  # 生成したグラフを表示