#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#05. n-gram
def n_gram(sequence,n):
    return [sequence[i:i+n] for i in range(len(sequence) - n+ 1)]

str1 = 'I am an NLPer'
tri_gram = n_gram(str1,3)
print(tri_gram)

bi_gram = n_gram(str1.split(),2)
print(bi_gram)

