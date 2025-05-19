from knock30 import parse_text_to_lines
lines = parse_text_to_lines("merosu_short.txt")

# 形態素トークンのリスト（表層形, 品詞）
tokens = []
for line in lines:
    if not line.strip() or line.startswith("EOS") or line.startswith("B"):
        continue
    parts = line.split()
    if len(parts) >= 4:
        surface = parts[0]
        pos = parts[4]
        tokens.append((surface, pos))

# 「名詞＋の＋名詞」パターンを抽出
print("🔍 名詞句（名詞+の+名詞）:")
for i in range(len(tokens) - 2):
    first, second, third = tokens[i], tokens[i+1], tokens[i+2]
    if first[1].startswith("名詞") and second[0] == "の" and third[1].startswith("名詞"):
        phrase = first[0] + second[0] + third[0]
        print(phrase)
