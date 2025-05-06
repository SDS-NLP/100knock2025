import json
import re

# JSONファイルを読み込む
with open('uk_article.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

text = data['text']

# 正規表現でメディアファイル名を抽出（ファイル: に対応）
media_pattern = r'\[\[ファイル:([^|\]]+)'
media_files = re.findall(media_pattern, text)

# 重複を取り除く（必要であれば）
# media_files = list(set(media_files))

# 結果を表示
print("📁 参照されているメディアファイル一覧：\n")
for filename in media_files:
    print(filename.strip())

# 件数を表示
print(f"\n🔢 メディアファイルの数: {len(media_files)} 件")
