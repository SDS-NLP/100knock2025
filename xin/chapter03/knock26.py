import json
import gzip
import re
from knock20 import uk_data
from knock25 import extract_template

uk_text = uk_data()
info_dict = extract_template(uk_text)

def remove_emphasis(info_dict):
    # 強調マークアップの正規表現パターン
    pattern = r"''+(.*?)''+"

    # 各値から強調を削除
    cleaned_dict = {}
    for k, v in info_dict.items():
        cleaned_value = re.sub(pattern, r"\1", v)
        cleaned_dict[k] = cleaned_value
    return cleaned_dict

# 強調除去後の辞書
cleaned_info_dict = remove_emphasis(info_dict)

# 結果確認（例：すべて表示）
for k, v in cleaned_info_dict.items():
    print(f"{k}: {v}")