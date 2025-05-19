#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re
import gzip
import json

with gzip.open('/Users/niaomuqing/Downloads/jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        article = json.loads(line)
        if article.get('title') == 'イギリス':
            text = article.get('text')
            break

for line in text.split('\n'):
    if re.search(r'\[\[Category:.*\]\]', line):
        print(line)

