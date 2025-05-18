#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

with open('/Users/niaomuqing/Downloads/popular-names.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

random.shuffle(lines)

for line in lines:
    print(line)
#shuf /Users/niaomuqing/Downloads/popular-names.txt

