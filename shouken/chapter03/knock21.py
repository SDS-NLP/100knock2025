import json
import re

file_path = 'jawiki-country.json'

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        article_data = json.loads(line)
        if article_data.get('title') == 'イギリス':
            article_text = article_data.get('text')
            break

for line in article_text.split('\n'):
    if '[[Category:' in line:
        print(line)

