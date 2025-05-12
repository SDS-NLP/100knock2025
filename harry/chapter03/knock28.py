import json
import re
import csv

# ---------------------------------------
# MediaWikiマークアップ除去関数
# ---------------------------------------
def clean_markup(value):
    # 0. ファイルリンク処理 [[ファイル:画像名|...]] → 画像名だけ
    value = re.sub(r'\[\[(?:ファイル|File):([^|\]]+).*?\]\]', r'\1', value)
    
    # 1. 強調マークアップ '' や ''' を削除
    value = re.sub(r"''+", '', value)

    # 2. 内部リンク [[表示|リンク先]] → 表示、[[リンク]] → リンク
    value = re.sub(r'\[\[([^|\]]+\|)?([^\]]+?)\]\]', r'\2', value)

    # 3. <ref>...</ref> の削除
    value = re.sub(r'<ref[^>]*>.*?</ref>', '', value, flags=re.DOTALL)

    # 4. HTMLタグ（<br>など）を削除
    value = re.sub(r'<.*?>', '', value)

    # 5. テンプレート {{lang|xx|表示}} → 表示
    value = re.sub(r'\{\{lang\|[^\|]*\|([^\}]+)\}\}', r'\1', value)

    # 6. その他テンプレート {{...}} を削除（ネストなし）
    value = re.sub(r'\{\{[^{}]*\}\}', '', value)

    # 7. 外部リンク [http://xxxx 説明] → 説明のみ or 削除
    value = re.sub(r'\[https?:\/\/[^\s]+\s+([^\]]+)\]', r'\1', value)
    value = re.sub(r'\[https?:\/\/[^\]]+\]', '', value)

    # 8. ゴミのような >xxx 残骸の除去
    value = re.sub(r'>[^<>\n]{10,}', '', value)

    # 9. 空白・改行を整形
    value = re.sub(r'\n+', ' ', value)
    value = re.sub(r'\s{2,}', ' ', value)

    return value.strip()

# ---------------------------------------
# JSON読み込み
# ---------------------------------------
with open('uk_article.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

text = data['text']

# ---------------------------------------
# 基礎情報テンプレートの抽出
# ---------------------------------------
infobox_match = re.search(r'{{基礎情報.*?\n(.*?)\n}}', text, re.DOTALL)
if not infobox_match:
    print("❌ 基礎情報テンプレートが見つかりませんでした。")
    exit()

infobox_body = infobox_match.group(1)

# フィールドの抽出
field_pattern = re.findall(r'\n\|([^=]+?)\s*=\s*(.*?)(?=\n\||\n$)', infobox_body, re.DOTALL)

# 辞書に格納（整形済み）
infobox_dict = {}
for name, value in field_pattern:
    clean_value = clean_markup(value)
    infobox_dict[name.strip()] = clean_value

# ---------------------------------------
# 結果表示
# ---------------------------------------
print("✅ 整形済みの基礎情報テンプレート：\n")
for key, val in infobox_dict.items():
    print(f"{key} : {val}")

# ---------------------------------------
# JSON形式で保存
# ---------------------------------------
with open('cleaned_infobox.json', 'w', encoding='utf-8') as f_json:
    json.dump(infobox_dict, f_json, ensure_ascii=False, indent=2)

# ---------------------------------------
# CSV形式で保存
# ---------------------------------------
with open('cleaned_infobox.csv', 'w', encoding='utf-8', newline='') as f_csv:
    writer = csv.writer(f_csv)
    writer.writerow(['フィールド名', '値'])
    for key, val in infobox_dict.items():
        writer.writerow([key, val])

print("✅ 整形済みの基礎情報を 'cleaned_infobox.json' および 'cleaned_infobox.csv' に保存しました。")