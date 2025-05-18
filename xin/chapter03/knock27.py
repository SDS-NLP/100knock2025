import json
import gzip
import re
from knock20 import uk_data
from knock25 import extract_template
from knock26 import remove_emphasis

uk_text = uk_data()
info_dict = extract_template(uk_text)
cleaned_info_dict = remove_emphasis(info_dict)

def remove_internal_links(info_dict):
    # 正規表現パターン： [[記事名|表示名]] or [[表示名]]
    pattern = r"\[\[(?:[^|\]]*\|)?([^|\]]+)\]\]"

    cleaned_dict = {}
    for k, v in info_dict.items():
        cleaned_value = re.sub(pattern, r"\1", v)
        cleaned_dict[k] = cleaned_value
    return cleaned_dict

cleaned_info_dict2 = remove_internal_links(cleaned_info_dict)

# 結果の表示（例：すべて）
for k, v in cleaned_info_dict2.items():
    print(f"{k}: {v}")