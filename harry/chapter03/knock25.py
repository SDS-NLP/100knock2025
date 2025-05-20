import json
import re

# イギリス記事のJSON読み込み
with open('uk_article.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

text = data['text']

# 1. 基礎情報テンプレートの全体を抽出（最初にマッチする {{基礎情報 ... }} を対象）
infobox_match = re.search(r'{{基礎情報.*?\n(.*?)\n}}', text, re.DOTALL)

if not infobox_match:
    print("❌ 基礎情報テンプレートが見つかりませんでした。")
    exit()

infobox_body = infobox_match.group(1)

# 2. 各フィールド（|名前 = 値）の抽出
field_pattern = re.findall(r'\n\|([^=]+?)\s*=\s*(.*?)(?=\n\||\n$)', infobox_body, re.DOTALL)

# 3. 辞書に格納
infobox_dict = {}
for name, value in field_pattern:
    infobox_dict[name.strip()] = value.strip()

# 4. 表示（確認）
for key, val in infobox_dict.items():
    print(f"{key} : {val}")
