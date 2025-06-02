#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gensim.models import KeyedVectors

model_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

analogy_file = "/Users/niaomuqing/100knock2025/questions-words.txt"

results = []

with open(analogy_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith(":"):
            section = line
            if section == ": capital-common-countries":
                in_section = True
            else:
                in_section = False
            continue

        if not in_section:
            continue

        w1, w2, w3, _ = line.split()

        if w1 not in model or w2 not in model or w3 not in model:
            results.append((w1, w2, w3, "*OOV*", 0.0))
            continue

        predicted, similarity = model.most_similar(positive=[w2, w3], negative=[w1], topn=1)[0]
        results.append((w1, w2, w3, predicted, similarity))

for r in results:
    print(f"{r[0]:<12} {r[1]:<12} {r[2]:<12} -> {r[3]:<15} (cosine: {r[4]:.4f})")

