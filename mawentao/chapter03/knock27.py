#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import gzip
import json

with gzip.open('/Users/niaomuqing/Downloads/jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        article = json.loads(line)
        if article['title'] == 'イギリス':
            text = article['text']
            break

template_match = re.search(r'{{基礎情報 国.*?^}}$', text, re.MULTILINE | re.DOTALL)
if not template_match:
    print("テンプレート見つけませんでした")
    exit()

template = template_match.group()

pattern = r'^\|(.+?)\s*=\s*(.+?)(?=\n\||\n$)'
fields = dict(re.findall(pattern, template, re.MULTILINE | re.DOTALL))

def clean_markup(value):
    value = re.sub(r"'{2,5}", '', value)
    value = re.sub(r'\[\[([^|\]]+?\|)?([^|\]]+?)\]\]', r'\2', value)

    return value

for key, value in fields.items():
    cleaned = clean_markup(value)
    print(f'{key} : {cleaned}')


