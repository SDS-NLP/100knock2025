import CaboCha
import os

# 初期化
cabocha = CaboCha.Parser()

# ファイルパス
base_dir = os.path.expanduser("~/100knock/100knock2025/harry/chapter04")
file_path = os.path.join(base_dir, "merosu_short.txt")

# 形態素が動詞かどうかを判定する関数
def is_verb(token_feature):
    return "動詞" in token_feature

# 係り受け処理
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        tree = cabocha.parse(line)

        chunks = {}
        tokens = {}

        # 文節情報を収集
        for i in range(tree.chunk_size()):
            chunk = tree.chunk(i)
            surface = ""
            token_features = []
            for j in range(chunk.token_pos, chunk.token_pos + chunk.token_size):
                token = tree.token(j)
                surface += token.surface
                token_features.append(token.feature)
            chunks[i] = {"text": surface, "link": chunk.link}
            tokens[i] = token_features

        # 主語が「メロス」の場合、述語を抽出
        for i, chunk in chunks.items():
            if "メロス" in chunk["text"]:
                dst = chunk["link"]
                if dst != -1:
                    dst_feats = tokens[dst]
                    if any(is_verb(feat) for feat in dst_feats):
                        print(f"{chunk['text']} → {chunks[dst]['text']}")
