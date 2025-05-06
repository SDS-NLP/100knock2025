import MeCab
import os

# ファイルパスと辞書パス
base_dir = os.path.expanduser("~/100knock/100knock2025/harry/chapter04")
text_file = os.path.join(base_dir, "kokoro_cleaned.txt")
unidic_path = os.path.expanduser("~/unidic-cwj")
mecabrc_path = "/etc/mecabrc"

# MeCabのTagger初期化（フォーマット指定）
# 出力をTSVとして扱えるようにし、node-format-chamame2を使用
  
mecab = MeCab.Tagger(
    f"-r {mecabrc_path} -d {unidic_path} "
    "-F '\\t%m\\t%f[7]\\t%f[6]\\t%f[23]\\t%F-[0,1,2,3]\\t%f[4]\\t%f[5]\\t%f[8]\\t%f[9]\\t%f[12]\\t%f[28]\\n' "
    "--unk-format='\\t%m\\t\\t\\t未知語\\t\\t\\n'"
)
mecab.parse("")  # 初期化バグ対策

# テキスト読み込み
with open(text_file, "r", encoding="utf-8") as f:
    text = f.read()

# MeCab解析結果を行単位で取得
output = mecab.parse(text)
lines = output.strip().split("\n")

#print("📄 形態素解析結果の例（先頭5行）:")
#for line in lines[:5]:  # 最初の5行を確認
#    print(line)

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

