#!/usr/bin/env python
# coding: utf-8

# In[ ]:


with open('/Users/niaomuqing/Downloads/popular-names.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines[:10]:
        print(line) 

#head -n 10 /Users/niaomuqing/Downloads/popular-names.txt

