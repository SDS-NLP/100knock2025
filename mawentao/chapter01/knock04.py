#!/usr/bin/env python
# coding: utf-8

# In[1]:


#04. 元素記号
str1 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
str2 = str1.replace('.','')
list_origin = str2.split()
len1 = len(list_origin)
print(len1)

first21 = list_origin[1:5]
first22 = list_origin[9:15]
first23 = [list_origin[19]]

list_first2 = first21 + first22 + first23
list_first1 = [x for x in list_origin if x not in list_first2]

first1 = [y[0] for y in list_first1]
first2 = [z[:2] for z in list_first2]

index1 = [list_origin.index(y) + 1 for y in list_first1]
index2 = [list_origin.index(z) + 1 for z in list_first2]

dict1 = dict(zip(first1,index1))
dict2 = dict(zip(first2,index2))

dict_final = dict1 | dict2

print(dict_final)


# In[ ]:


#04.1
str1 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
str2 = str1.replace('.','')
list_origin = str2.split()
len1 = len(list_origin)
print(len1)

first21 = list_origin[1:5]
first22 = list_origin[9:15]
first23 = [list_origin[19]]

list_first2 = first21 + first22 + first23
list_first1 = [x for x in list_origin if x not in list_first2]

dict_final = {}

for i, word in enumerate(list_origin, start = 1):
    if word in list_first1:
        key = word[0]
    else:
        key = word[:2]
    dict_final[key] = i

print(dict_final)

