#!/usr/bin/env python
# coding: utf-8

# In[2]:


import MeCab
from collections import Counter
import math

with open('/Users/niaomuqing/100knock2025/kokoro.txt', 'r', encoding='utf-8') as f:
    text = f.read()

documents = [doc.strip() for doc in text.split('\n\n') if doc.strip()]

tagger = MeCab.Tagger('-Ochasen')

def extract_nouns(text):
    nouns = []
    node = tagger.parseToNode(text)
    while node:
        features = node.feature.split(',')
        if features[0] == '名詞':
            nouns.append(node.surface)
        node = node.next
    return nouns

docs_nouns = [extract_nouns(doc) for doc in documents]

all_nouns = [noun for doc in docs_nouns for noun in doc]
tf_counter = Counter(all_nouns)
total_terms = sum(tf_counter.values())
tf = {word: count / total_terms for word, count in tf_counter.items()}

doc_count = len(docs_nouns)
df = {}
for doc in docs_nouns:
    for word in set(doc):  
        df[word] = df.get(word, 0) + 1

idf = {word: math.log(doc_count / df[word]) for word in df}

tfidf = {word: tf[word] * idf[word] for word in tf if word in idf}

top_words = sorted(tfidf.items(), key=lambda x: x[1], reverse=True)[:20]

print(f"{'词':<10}{'TF':>10}{'IDF':>10}{'TF-IDF':>10}")
for word, score in top_words:
    print(f"{word:<10}{tf[word]:>10.6f}{idf[word]:>10.6f}{score:>10.6f}")


# In[ ]:




