#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import gzip
import json

with gzip.open('/Users/niaomuqing/Downloads/jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        article = json.loads(line)
        if article.get('title') == 'イギリス':
            text = article.get('text')
            break

pattern = r'\[\[(?:File|ファイル):(.+?)(?:\||\]\])'
files = re.findall(pattern, text)

for f in files:
    print(f)

