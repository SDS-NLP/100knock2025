# 文章textにおいて、「メロス」が主語であるときの述語を抽出せよ。
import CaboCha

# 解析対象テキスト（各行が１文）
text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

# CaboCha パーサを初期化
parser = CaboCha.Parser()

# 「メロス」が主語（「メロスは」「メロスには」）のときの述語を抽出
for line in text.strip().splitlines():
    tree = parser.parse(line)
    for i in range(tree.chunk_size()):
        chunk = tree.chunk(i)
        # 文節の表層形を取得
        origin = ''.join(
            tree.token(j).surface
            for j in range(chunk.token_pos, chunk.token_pos + chunk.token_size)
        )
        # 「メロスは」または「メロスには」で始まる文節を主語とみなす
        if origin.startswith("メロスは") or origin.startswith("メロスには"):
            dest_idx = chunk.link
            if dest_idx != -1:
                # 係り先（述語）の表層形を取得
                dest_chunk = tree.chunk(dest_idx)
                predicate = ''.join(
                    tree.token(j).surface
                    for j in range(dest_chunk.token_pos, dest_chunk.token_pos + dest_chunk.token_size)
                )
                print(predicate)
