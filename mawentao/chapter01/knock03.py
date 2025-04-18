#!/usr/bin/env python
# coding: utf-8

# In[14]:


#03. 円周率
str1 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
str2 = str1.replace(',', '')
str3 = str2.replace('.', '')
list1 = str3.split()

mojisu = []
for i in list1:
    mojisu.append(len(i))

print(mojisu)

