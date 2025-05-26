import gzip
import json

path = 'daiki/chapter03/jawiki-country.json.gz'

uk_text = ""
with gzip.open(path, 'rt', encoding = 'utf-8') as file:
    for line in file:
        article = json.loads(line)
        if article['title'] == 'イギリス':
            uk_text = article['text']
            break
category_lines = [line for line in uk_text.split('\n') if '[[Category:' in line]
if __name__ == "__main__":

   for line in category_lines:
      print(line)