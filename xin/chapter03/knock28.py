import re
from knock20 import uk_data
from knock25 import extract_template
from knock26 import remove_emphasis
from knock27 import remove_internal_links

# 基本情報の抽出と前処理
uk_text = uk_data()
info_dict = extract_template(uk_text)
cleaned_info_dict = remove_emphasis(info_dict)
cleaned_info_dict = remove_internal_links(cleaned_info_dict)

def remove_markup(info_dict):
    cleaned_dict = {}
    for key, value in info_dict.items():
        text = value

        # <ref>タグ（内容あり・なし）を除去
        text = re.sub(r'<ref[^>]*>.*?</ref>', '', text)
        text = re.sub(r'<ref[^>]*/>', '', text)

        # <br>や<br />などの改行タグ除去
        text = re.sub(r'<br\s*/?>', '', text)

        # {{lang|xx|文字列}} → 文字列 に変換
        text = re.sub(r'\{\{lang\|[^\|]+\|([^\}]+)\}\}', r'\1', text)

        # その他のテンプレート系（例：{{仮リンク|〇〇}}）などの簡易除去
        text = re.sub(r'\{\{[^}]+\}\}', '', text)

        # HTMLエンティティも必要に応じて処理
        text = text.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')

        cleaned_dict[key] = text.strip()
    return cleaned_dict

final_cleaned_info = remove_markup(cleaned_info_dict)

# 表示（必要に応じて整形）
for k, v in final_cleaned_info.items():
    print(f"{k}: {v}")