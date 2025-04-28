#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = 10

with open('/Users/niaomuqing/Downloads/popular-names.txt', 'r', encoding='utf-8') as f:
    for i in range(N):
        line = f.readline()
        str = line.split('\t')  
        if len(str) > 0:
            print(str[0]) 

#head -n 10 /Users/niaomuqing/Downloads/popular-names.txt | cut -f 1



# In[ ]:




