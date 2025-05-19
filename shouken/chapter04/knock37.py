from collections import Counter
from fugashi import GenericTagger

tagger = GenericTagger("-r /etc/mecabrc -d /var/lib/mecab/dic/debian")

with open("kokoro.txt", encoding="utf-8") as f:
    text = f.read()

# 品詞が「名詞」のみ抽出
nouns = [word.surface for word in tagger(text) if word.feature[0] == "名詞"]

counter = Counter(nouns)

for word, freq in counter.most_common(20):
    print(f"{word}\t{freq}")
