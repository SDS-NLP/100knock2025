import json

file_path = 'jawiki-country.json'

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        article_data = json.loads(line)
        if article_data.get('title') == 'イギリス':
            article_text = article_data.get('text')
            break

for line in article_text.split('\n'):
    line = line.strip()

    if line.startswith('=') and line.endswith('='):
        equals_each_side = line.count('=') // 2
        level = equals_each_side - 1
        section_title = line.strip('=').strip()

        print(f'レベル{level}：{section_title}')
