import json

file_path = 'jawiki-country.json'

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        article = json.loads(line)
        if article.get('title') == 'イギリス':
            uk_text = article.get('text')
            print(uk_text)
            break
