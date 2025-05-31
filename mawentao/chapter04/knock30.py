#!/usr/bin/env python
# coding: utf-8

# In[4]:


import MeCab
with open('/Users/niaomuqing/100knock2025/走れメロス.txt', 'r', encoding='utf-8') as f:
    text = f.read()

mecab = MeCab.Tagger('-r /opt/homebrew/etc/mecabrc')
node = mecab.parseToNode(text)
while node:
    if node.surface != "":
        features = node.feature.split(',')
        if features[0] == '動詞':
            print(node.surface)
    node = node.next


# In[ ]:




