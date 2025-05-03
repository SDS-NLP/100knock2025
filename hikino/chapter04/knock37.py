import MeCab
from collections import Counter

with open("../../../kokoro.txt", "r", encoding="utf-8") as f:
    text = f.read()

tagger = MeCab.Tagger("-Owakati -r /etc/mecabrc")
words = tagger.parse(text).strip().split()

node = tagger.parseToNode(text)

nouns = []

while node:
    features = node.feature.split(",")  
    if features[0] == "名詞":  
        nouns.append(node.surface)
    node = node.next

counter = Counter(nouns)
top20 = counter.most_common(20)
for word, count in top20:
    print(f"{word}: {count}")
    