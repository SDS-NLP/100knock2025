import knock20
import re

# 基礎情報テンプレートの内容全体を抽出
pattern = r'\{\{基礎情報.*?\n(.*?)\n\}\}'  # 基礎情報テンプレートの中身を非貪欲に抜く
template_text = re.search(pattern, knock20.uk_text, re.DOTALL).group(1)

# フィールド名と値を辞書に抽出
pattern_field = r'\n\|(.*?)\s*=\s*(.*?)(?=\n\||\n$)'  # フィールド名=値 をマッチ（次の | か終端まで）
fields = re.findall(pattern_field, template_text, re.DOTALL)

# 結果を辞書に格納
infobox = {key.strip(): value.strip() for key, value in fields}

# 確認
for k, v in infobox.items():
    print(f'{k}: {v}')
