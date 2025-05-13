import json
import gzip
import re
from knock20 import uk_data

def extract_template(text):
    # 基礎情報テンプレートを抽出
    pattern = r"{{基礎情報 国(.*?)\n}}"
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return {}
    basic_info = match.group(1)

    # 各フィールドを抽出
    pattern1 = r"\|(.+?)\s*=\s*(.*?)(?=\n\||\n$)"
    fields = re.findall(pattern1, basic_info, re.DOTALL)

    # 辞書に格納
    info_dict = {field[0].strip(): field[1].strip() for field in fields}
    return info_dict

# 呼び出し
uk_text = uk_data()
info_dict = extract_template(uk_text)
print(info_dict)