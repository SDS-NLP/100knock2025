import json
import re

def load_uk_article(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            article = json.loads(line)
            if article.get('title') == 'イギリス':
                return article.get('text')
    return None

def extract_template_lines(article_text):
    in_template = False
    lines = []

    for line in article_text.split('\n'):
        if line.startswith('{{基礎情報'):
            in_template = True
        elif line.startswith('}}') and in_template:
            lines.append(line)
            break
        if in_template:
            lines.append(line)

    return lines

def clean_value(value):
    # 強調マークアップ（''〜''）の除去
    for count in range(5, 1, -1):
        value = value.replace("'" * count, '')

    # HTMLタグや特殊文字の除去・置換
    value = value.replace('<br />', '\n').replace('<br>', '\n')
    value = re.sub(r'<ref.*?>.*?</ref>', '', value)
    value = value.replace('&nbsp;', ' ')

    # 内部リンク [[A|B]] → B, [[A]] → A
    def clean_internal_link(match):
        inner = match.group(1)
        return inner.split('|')[-1] if '|' in inner else inner

    value = re.sub(r'\[\[([^\]]+)\]\]', clean_internal_link, value)

    # 外部リンク [http://xxx 説明文] → 説明文
    value = re.sub(r'\[http[^\s]*\s([^\]]+)\]', r'\1', value)

    # {{lang|en|text}} → text
    value = re.sub(r'\{\{lang\|[^\|]+\|([^\}]+)\}\}', r'\1', value)

    # {{仮リンク|表示名|記事名}} → 表示名
    value = re.sub(r'\{\{仮リンク\|([^\|]+)\|[^\}]+\}\}', r'\1', value)

    # その他テンプレート（{{...}}）はまとめて削除
    value = re.sub(r'\{\{.*?\}\}', '', value)

    return value.strip()

def parse_template(template_lines):
    info_dict = {}

    for line in template_lines:
        if line.startswith('|'):
            parts = line[1:].split(' = ', 1)
            if len(parts) == 2:
                field_name = parts[0].strip()
                raw_value = parts[1].strip()
                cleaned_value = clean_value(raw_value)
                info_dict[field_name] = cleaned_value

    return info_dict

file_path = 'jawiki-country.json'

article_text = load_uk_article(file_path)
template_lines = extract_template_lines(article_text)
info_dict = parse_template(template_lines)

for name, value in info_dict.items():
    print(f'{name}:\n{value}\n{"-" * 40}')
