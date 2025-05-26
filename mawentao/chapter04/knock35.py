#!/usr/bin/env python
# coding: utf-8

# In[2]:


import CaboCha

parser = CaboCha.Parser()
sentence = "メロスは激怒した。"
tree = parser.parse(sentence)

print(tree.toString(CaboCha.FORMAT_TREE))


# In[ ]:




