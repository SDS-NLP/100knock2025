#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gensim.models import KeyedVectors

model_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

results = model.most_similar(positive=["Athens", "Spain"], negative=["Madrid"], topn=10)

for word, similarity in results:
    print(f"{word}: {similarity:.4f}")

