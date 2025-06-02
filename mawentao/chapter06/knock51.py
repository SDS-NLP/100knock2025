#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import dot
from numpy.linalg import norm
from gensim.models import KeyedVectors

model_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin" 
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

vec_us = model["United_States"]
vec_usa = model["U.S."]

cos_sim = dot(vec_us, vec_usa) / (norm(vec_us) * norm(vec_usa))

print("cosine(United_States, U.S.) =", cos_sim)

