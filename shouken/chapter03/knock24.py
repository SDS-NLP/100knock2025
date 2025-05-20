import json

file_path = 'jawiki-country.json'

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        article_data = json.loads(line)
        if article_data.get('title') == 'イギリス':
            article_text = article_data.get('text')
            break

for line in article_text.split('\n'):
    if '[[File:' in line or '[[ファイル:' in line:
        parts = line.split('[[')

        for part in parts:
            if part.startswith('File:') or part.startswith('ファイル:'):
                start_index = part.find(':') + 1
                end_index = part.find('|')

                if end_index == -1:
                    end_index = part.find(']]')

                file_name = part[start_index:end_index].strip()

                print(file_name)
