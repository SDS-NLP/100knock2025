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

for line in text.split('\n'):
    match = re.match(r'^(={2,})\s*(.+?)\s*\1$', line)
    if match:
        level = len(match.group(1)) - 1 
        title = match.group(2)
        print(f'{title} (level {level})')

