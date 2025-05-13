import MeCab
import os

# パス設定
base_dir = os.path.expanduser("~/100knock/100knock2025/harry/chapter04")
text_file = os.path.join(base_dir, "kokoro_cleaned.txt")
unidic_path = os.path.expanduser("~/unidic-cwj")
mecabrc_path = "/etc/mecabrc"

# MeCab 初期化（Chamame2フォーマット）
mecab = MeCab.Tagger(
    f"-r {mecabrc_path} -d {unidic_path} "
    "-F '\\t%m\\t%f[7]\\t%f[6]\\t%f[0]\\n' "  # 表層形、語彙素、語形、品詞
    "--unk-format='\\t%m\\t\\t\\t未知語\\n'"
)
mecab.parse("")

# ファイル読み込み
with open(text_file, "r", encoding="utf-8") as f:
    text = f.read()

# MeCabで解析 → 行ごとの形態素情報を取得
output = mecab.parse(text)
lines = output.strip().split("\n")

# 形態素トークンのリスト（表層形, 品詞）
tokens = []
for line in lines:
    if not line.strip() or line.startswith("EOS") or line.startswith("B"):
        continue
    parts = line.split()
    if len(parts) >= 4:
        surface = parts[0]
        pos = parts[3]
        tokens.append((surface, pos))

# 「名詞＋の＋名詞」パターンを抽出
print("🔍 名詞句（名詞+の+名詞）:")
for i in range(len(tokens) - 2):
    first, second, third = tokens[i], tokens[i+1], tokens[i+2]
    if first[1].startswith("名詞") and second[0] == "の" and third[1].startswith("名詞"):
        phrase = first[0] + second[0] + third[0]
        print(phrase)
