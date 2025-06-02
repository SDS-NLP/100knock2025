import CaboCha
import knock30

text = knock30.text
# CaboChaの初期化
parser = CaboCha.Parser()

# 解析結果を取得
tree = parser.parse(text)

# 結果をタブ区切りで表示
for i in range(tree.chunk_size()):
    chunk = tree.chunk(i)
    if chunk.link != -1:  # 係り先がある場合のみ
        src_tokens = "".join([tree.token(j).surface for j in range(chunk.token_pos, chunk.token_pos + chunk.token_size)])
        dst_tokens = "".join([tree.token(j).surface for j in range(tree.chunk(chunk.link).token_pos, tree.chunk(chunk.link).token_pos + tree.chunk(chunk.link).token_size)])
        print(f"{src_tokens}\t{dst_tokens}")