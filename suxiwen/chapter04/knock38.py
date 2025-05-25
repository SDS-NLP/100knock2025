import re
import MeCab
import math
from collections import Counter, defaultdict

with open("../../../kokoro.txt", "r", encoding="utf-8") as f:
    text = f.read()

chapters = re.split(r'(?=^[一二三四五六七八九十百]+\n)', text, flags=re.MULTILINE)
chapters = [ch.strip() for ch in chapters if ch.strip()]
first = chapters[0]
first = first.replace("\ufeff", "")
chapters[0] = first

chapters = [text.replace("\n", "") for text in chapters]
chapters = [text[1:] for text in chapters]

dct = defaultdict(int)
counters = []

tagger = MeCab.Tagger("-Owakati -r /etc/mecabrc")

for text in chapters:
  words = tagger.parse(text).strip().split()
  counter = Counter(words)
  counters.append(counter)
  for word in set(words):
    dct[word] += 1

idf = {word: math.log(len(chapters) / (1 + dct[word])) for word in dct}

tfidf_list = []
for counter in counters:
    total_terms = sum(counter.values())
    tfidf = {
        word: (number / total_terms) * idf[word]
        for word, number in counter.items()
    }
    tfidf_list.append(tfidf)

total_scores = defaultdict(float)
for tfidf in tfidf_list:
    for word, score in tfidf.items():
        total_scores[word] += score

top_20 = sorted(total_scores.items(), key=lambda x: x[1], reverse=True)[:20]
for word, score in top_20:
    print(f"{word}\tTF-IDF: {score:.4f}")