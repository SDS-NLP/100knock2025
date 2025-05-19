import json
import re

# -----------------------------
# ヘルパー関数: MediaWikiマークアップ除去
# -----------------------------

def clean_markup(value):
    # 1. 強調マークアップ除去: '' や ''' など
    value = re.sub(r"''+", '', value)

    # 2. 内部リンク: [[表示名|リンク先]] → 表示名、[[リンク]] → リンク
    value = re.sub(r'\[\[([^|\]]+?\|)?(.+?)\]\]', r'\2', value)

    # 3. HTMLタグの除去: <ref>...</ref>, <br />, など
    value = re.sub(r'<.*?>', '', value)

    # 4. テンプレート: {{lang|en|United Kingdom}} → United Kingdom
    value = re.sub(r'\{\{.*?\|.*?\|(.+?)\}\}', r'\1', value)

    # 5. その他の波かっこテンプレートの簡易除去: {{〜}} → 空に
    value = re.sub(r'\{\{.*?\}\}', '', value)

    return value.strip()

# -----------------------------
# メイン処理
# -----------------------------

# JSON読み込み
with open('uk_article.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

text = data['text']

# 基礎情報テンプレートの抽出
infobox_match = re.search(r'{{基礎情報.*?\n(.*?)\n}}', text, re.DOTALL)
if not infobox_match:
    print("❌ 基礎情報テンプレートが見つかりませんでした。")
    exit()

infobox_body = infobox_match.group(1)

# フィールド抽出: |フィールド名 = 値
field_pattern = re.findall(r'\n\|([^=]+?)\s*=\s*(.*?)(?=\n\||\n$)', infobox_body, re.DOTALL)

# 辞書に格納（整形付き）
infobox_dict = {}
for name, value in field_pattern:
    clean_value = clean_markup(value)
    infobox_dict[name.strip()] = clean_value

# 結果表示
print("✅ 整形済みの基礎情報テンプレート：\n")
for key, val in infobox_dict.items():
    print(f"{key} : {val}")
