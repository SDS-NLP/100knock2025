#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import Counter

with open('/Users/niaomuqing/Downloads/popular-names.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
first = [line.split('\t')[0] for line in lines]
counter = Counter(first)
for x, count in counter.most_common():
    print(count, x)
#cut -f 1 /Users/niaomuqing/Downloads/popular-names.txt | sort | uniq -c | sort -nr

