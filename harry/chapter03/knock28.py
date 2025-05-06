import json
import re
import csv

# -----------------------------
# ヘルパー関数: MediaWikiマークアップ除去
# -----------------------------

def clean_markup(value):
    # 強調マークアップ '' や ''' を削除
    value = re.sub(r"''+", '', value)

    # 内部リンク [[表示|リンク先]] → 表示、[[リンク]] → リンク
    value = re.sub(r'\[\[([^|\]]+\|)?([^\]]+)\]\]', r'\2', value)

    # 外部リンク [http://xxxx 説明] → 完全削除（説明も削除）
    value = re.sub(r'\[https?:\/\/[^\]]+\]', '', value)

    # テンプレート {{lang|xx|表示}} → 表示
    value = re.sub(r'\{\{lang\|[^\|]*\|([^\}]+)\}\}', r'\1', value)

    # その他テンプレート {{...}} → 削除（ネストしない前提）
    value = re.sub(r'\{\{[^{}]*\}\}', '', value)

    # HTMLタグ <ref>...</ref>、<br>、<sup> などを削除
    value = re.sub(r'<.*?>', '', value)

    # パイプと = を含む不要な残骸を削除（例: |title=xxx）
    value = re.sub(r'\|\s*[a-zA-Z0-9_]+ *= *[^|]+', '', value)

    # 明らかにゴミっぽい > を含む長い文（残骸）を削除（例: IMF>Data and Statistics...）
    value = re.sub(r'>[^<>\n]{10,}', '', value)

    # 不要な空白や改行を整理
    value = re.sub(r'\n+', ' ', value)
    value = re.sub(r'\s{2,}', ' ', value)

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

# -----------------------------
# JSON形式で保存
# -----------------------------
with open('cleaned_infobox.json', 'w', encoding='utf-8') as f_json:
    json.dump(infobox_dict, f_json, ensure_ascii=False, indent=2)

# -----------------------------
# CSV形式で保存（1列目: フィールド名, 2列目: 値）
# -----------------------------
with open('cleaned_infobox.csv', 'w', encoding='utf-8', newline='') as f_csv:
    writer = csv.writer(f_csv)
    writer.writerow(['フィールド名', '値'])
    for key, val in infobox_dict.items():
        writer.writerow([key, val])

print("✅ 整形済み基礎情報を 'cleaned_infobox.json' および 'cleaned_infobox.csv' に保存しました。")