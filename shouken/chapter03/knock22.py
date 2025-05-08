import json

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
    for line in f:
        article = json.loads(line)
        if article['title'] == 'イギリス':
            uk_text = article['text']
            break

for line in uk_text.split('\n'):
    if '[[Category:' in line:
        line = line.strip() 
        start = line.find('[[Category:') + len('[[Category:')
        end = line.find('|') 
        if end == -1:
            end = line.find(']]') 
        category_name = line[start:end]
        print(category_name)
