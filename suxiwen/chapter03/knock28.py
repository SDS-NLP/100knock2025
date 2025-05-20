import re

def remove_markup(value):
    value = re.sub(r'\[\[([^|]*?)\|?([^]]*?)\]\]', r'\2' if r'\2' else r'\1', value)  # 内部リンク
    value = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', value)  # 外部リンク
    value = re.sub(r'<.*?>', '', value)  # HTMLタグ
    value = re.sub(r'{{.*?}}', '', value)  # テンプレート
    value = re.sub(r'&.*?;', '', value)  # エンティティ
    return value.strip()

cleaned_data_28 = {k: remove_markup(v) for k, v in cleaned_data_27.items()}
for k, v in cleaned_data_28.items():
    print(f"{k}: {v}")