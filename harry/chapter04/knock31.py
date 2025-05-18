from knock30 import parse_text_to_lines
lines = parse_text_to_lines("merosu_short.txt")

print("🔍 動詞（表層形, 原形）:")
for line in lines:
    if not line.strip():
        continue
    try:
        cols = line.split()  # タブやスペースの混在に対応
        surface = cols[0]
        lemma = cols[1]
        pos = cols[4]  # 品詞（例：動詞-一般, 動詞-非自立可能）

        if pos.startswith("動詞"):
            print(f"{surface}、{lemma}")
    except IndexError:
        continue

