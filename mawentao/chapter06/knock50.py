#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from gensim.models import KeyedVectors

model_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin" 
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

print(model["United_States"])

