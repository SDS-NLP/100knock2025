#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import gzip
import json

with gzip.open('/Users/niaomuqing/Downloads/jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        article = json.loads(line)
        if article.get('title') == 'イギリス':
            text = article.get('text')
            break

categories = re.findall(r'\[\[Category:([^|\]]+)', text)

for namae in categories:
    print(namae)

