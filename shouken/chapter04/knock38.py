import json
import math
from collections import Counter
from fugashi import GenericTagger

tagger = GenericTagger("-r /etc/mecabrc -d /var/lib/mecab/dic/debian")

# ファイル読み込みと分割
target_title = "日本"
target_text = ""
other_docs = []

with open("jawiki-country.json", encoding="utf-8") as f:
    for line in f:
        article = json.loads(line)
        if article["title"] == target_title:
            target_text = article["text"]
        else:
            other_docs.append(article["text"])

# TF計算（日本記事の名詞頻度）
target_words = [w.surface for w in tagger(target_text) if w.feature[0] == "名詞"]
tf_counter = Counter(target_words)
tf_total = sum(tf_counter.values())

# IDF計算（他記事に何文書登場するか）
doc_count = len(other_docs)
idf_counter = Counter()

for text in other_docs:
    nouns_in_doc = set(w.surface for w in tagger(text) if w.feature[0] == "名詞")
    for noun in nouns_in_doc:
        idf_counter[noun] += 1

# TF-IDF計算
results = []
for word, tf in tf_counter.items():
    df = idf_counter[word]
    if df == 0:
        continue
    tf_score = tf / tf_total
    idf_score = math.log(doc_count / df)
    tfidf = tf_score * idf_score
    results.append((word, tf_score, idf_score, tfidf))

# 上位20語表示
results.sort(key=lambda x: x[3], reverse=True)

for word, tf, idf, tfidf in results[:20]:
    print(f"{word}\tTF: {tf:.5f}\tIDF: {idf:.5f}\tTF-IDF: {tfidf:.5f}")
