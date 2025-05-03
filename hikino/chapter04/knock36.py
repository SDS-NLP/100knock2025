import MeCab
from collections import Counter

with open("../../../kokoro.txt", "r", encoding="utf-8") as f:
    text = f.read()

tagger = MeCab.Tagger("-Owakati -r /etc/mecabrc")
words = tagger.parse(text).strip().split()

counter = Counter(words)

for word, freq in counter.most_common(20):
    print(f"{word}→{freq}")
