import json

file_path = 'jawiki-country.json'

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        article_data = json.loads(line)
        if article_data.get('title') == 'イギリス':
            article_text = article_data.get('text')
            break

in_template = False
template_lines = []

for line in article_text.split('\n'):
    if line.startswith('{{基礎情報'):
        in_template = True
    elif line.startswith('}}') and in_template:
        template_lines.append(line)
        break
    if in_template:
        template_lines.append(line)

info_dict = {}

for line in template_lines:
    if line.startswith('|'):
        parts = line[1:].split(' = ', 1)
        if len(parts) == 2:
            field_name = parts[0].strip()
            field_value = parts[1].strip()
            info_dict[field_name] = field_value

for name, value in info_dict.items():
    print(f'{name}:\n{value}\n{"-"*40}')
