from collections import Counter
from fugashi import GenericTagger

tagger = GenericTagger("-r /etc/mecabrc -d /var/lib/mecab/dic/debian")

with open("kokoro.txt", encoding="utf-8") as f:
    text = f.read()

words = [word.surface for word in tagger(text)]
counter = Counter(words)

for word, freq in counter.most_common(20):
    print(f"{word}\t{freq}")
