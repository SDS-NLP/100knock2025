import json

def load_uk_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
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

def clean_internal_links(text):
    while '[[' in text and ']]' in text:
        start = text.find('[[')
        end = text.find(']]', start)
        if end == -1:
            break

        content = text[start + 2:end]
        if '|' in content:
            replacement = content.split('|')[1]
        else:
            replacement = content

        text = text[:start] + replacement + text[end + 2:]
    return text

def clean_field_value(value):
    for i in range(5, 1, -1):
        value = value.replace("'" * i, '')

    value = value.replace('<br />', '\n').replace('<br>', '\n')
    value = value.replace('&nbsp;', ' ')
    value = value.replace('<ref>', '').replace('</ref>', '')

    value = clean_internal_links(value)

    return value.strip()

def extract_cleaned_template(file_path):
    article_text = load_uk_article(file_path)
    template_lines = extract_template_lines(article_text)
    info_dict = {}

    for line in template_lines:
        if line.startswith('|'):
            parts = line[1:].split(' = ', 1)
            if len(parts) == 2:
                field_name = parts[0].strip()
                raw_value = parts[1].strip()
                cleaned_value = clean_field_value(raw_value)
                info_dict[field_name] = cleaned_value

    return info_dict

file_path = 'jawiki-country.json'
cleaned_info = extract_cleaned_template(file_path)

for key, value in cleaned_info.items():
    print(f'{key}:\n{value}\n{"-" * 40}')
