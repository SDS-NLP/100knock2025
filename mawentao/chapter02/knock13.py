#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = 10

with open('/Users/niaomuqing/Downloads/popular-names.txt', 'r', encoding='utf-8') as f:
    for i in range(N):
        line = f.readline()
        line = line.replace('\t', ' ')
        print(line)
#head -n 10 /Users/niaomuqing/Downloads/popular-names.txt | tr '\t' ' '



# In[ ]:




