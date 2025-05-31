#!/usr/bin/env python
# coding: utf-8

# In[5]:


import MeCab
from collections import Counter

with open('/Users/niaomuqing/100knock2025/kokoro.txt', 'r', encoding='utf-8') as f:
    text = f.read()

tagger = MeCab.Tagger('-r /opt/homebrew/etc/mecabrc') 
parsed = tagger.parse(text)

lines = [line for line in parsed.splitlines() if line != 'EOS' and line.strip()]

word_counter = Counter()

for line in lines:
    surface, feature_str = line.split('\t')
    features = feature_str.split(',')
    base_form = features[6]
    if base_form == '*':
        base_form = surface
    word_counter[base_form] += 1

for word, freq in word_counter.most_common(20):
    print(f'{word}\t{freq}')


# In[ ]:




