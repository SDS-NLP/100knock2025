#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

if template_match:
    template = template_match.group() 

    pattern = r'^\|(.+?)\s*=\s*(.+?)(?=\n\||\n$)'
    fields = dict(re.findall(pattern, template, re.MULTILINE | re.DOTALL))

    for key, value in fields.items():
        print(f'{key.strip()} : {value.strip()}')
else:
    print("“基礎情報 国”見つけませんでした。")


# In[ ]:




