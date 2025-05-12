#!/usr/bin/env python
# coding: utf-8

# In[ ]:


with open('/Users/niaomuqing/Downloads/popular-names.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

first = set()

for line in lines:
    str = line.split('\t') 
    if str:
        first.add(str[0])

for dif in sorted(first):
    print(dif)
#cut -f 1 /Users/niaomuqing/Downloads/popular-names.txt | sort | uniq

