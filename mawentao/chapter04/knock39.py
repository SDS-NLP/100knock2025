#!/usr/bin/env python
# coding: utf-8

# In[2]:


import MeCab
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

with open('/Users/niaomuqing/100knock2025/kokoro.txt', 'r', encoding='utf-8') as f:
    text = f.read()

tagger = MeCab.Tagger('-Owakati')
words = tagger.parse(text).strip().split()

counter = Counter(words)
freqs = sorted(counter.values(), reverse=True)

ranks = np.arange(1, len(freqs) + 1)

plt.figure(figsize=(8, 6))
plt.loglog(ranks, freqs)
plt.xlabel('词的出現頻度順位（Rank）')
plt.ylabel('出現頻度（Frequency）')
plt.title('Zipfの法則に基づく両対数グラフ')
plt.grid(True)
plt.show()


# In[ ]:




