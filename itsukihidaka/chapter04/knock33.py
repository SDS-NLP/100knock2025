# 文章textに係り受け解析を適用し、係り元と係り先のトークン（形態素や文節などの単位）をタブ区切り形式ですべて抽出せよ。

import CaboCha

# 解析対象のテキスト
text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

parser = CaboCha.Parser()

# 各行（文）ごとに解析
for line in text.strip().splitlines():
    tree = parser.parse(line)
    for i in range(tree.chunk_size()):
        chunk = tree.chunk(i)
        dest_idx = chunk.link
        if dest_idx != -1:
            # 係り元文節の表層形を取得
            origin = ''.join(
                tree.token(j).surface
                for j in range(chunk.token_pos, chunk.token_pos + chunk.token_size)
            )
            # 係り先文節の表層形を取得
            dest_chunk = tree.chunk(dest_idx)
            target = ''.join(
                tree.token(j).surface
                for j in range(dest_chunk.token_pos, dest_chunk.token_pos + dest_chunk.token_size)
            )
            # タブ区切りで出力
            print(f"{origin}\t{target}")