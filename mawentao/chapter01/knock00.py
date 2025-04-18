#!/usr/bin/env python
# coding: utf-8

# In[4]:


#00. パタトクカシーー
str1 = 'パトカー'
str2 = 'タクシー'
result = []
for i in range(len(str1)):
    result.append(str1[i])
    result.append(str2[i])
result1 = ''.join(result)
print(result1)

