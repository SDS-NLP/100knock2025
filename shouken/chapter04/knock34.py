import CaboCha

with open("merosu.txt", encoding="utf-8") as f:
    text = f.read()

parser = CaboCha.Parser()

# 文ごとに分けて処理
for sentence in text.split("。"):
    if not sentence.strip():
        continue

    # 係り受け解析
    tree = parser.parse(sentence)

    chunks = {}       # 文節情報を格納
    chunk_id = -1     # 文節番号

    # 文節ごとに情報を構築
    for i in range(tree.size()):
        token = tree.token(i)

        # 文節の先頭がある場合は新しい文節と判断
        if token.chunk:
            chunk_id += 1
            chunks[chunk_id] = {
                "link": token.chunk.link,  # この文節が係る先
                "tokens": []               # この文節に含まれる形態素
            }

        # 文節に属する形態素を追加
        if chunk_id >= 0:
            chunks[chunk_id]["tokens"].append(token.surface)

    # 「メロス」を含む文節の係り先文節を探して表示
    for idx, chunk in chunks.items():
        chunk_surface = "".join(chunk["tokens"])
        if "メロス" in chunk_surface:
            dst = chunk["link"]
            if dst != -1 and dst in chunks:
                dst_surface = "".join(chunks[dst]["tokens"])
                print(dst_surface)
