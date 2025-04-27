#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open('/Users/niaomuqing/Downloads/popular-names.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
lines.sort(key=lambda line: int(line.split('\t')[2]), reverse=True)
for line in lines:
    print(line.strip())

#sort -k 3,3 -n -r /Users/niaomuqing/Downloads/popular-names.txt

