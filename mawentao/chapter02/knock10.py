#!/usr/bin/env python
# coding: utf-8

# In[ ]:


f = open('/Users/niaomuqing/Downloads/popular-names.txt', 'r', encoding = 'utf-8')
lines = f.readlines()
print(len(lines))
f.close()

#wc -l /Users/niaomuqing/Downloads/popular-names.txt

