#単語の出現頻度
import spacy
from collections import Counter

nlp = spacy.load("ja_ginza")

# 出現頻度カウント用
freq = Counter()

with open("kokoro.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        # 分割して1文ずつ処理
        try:
            doc = nlp(line)
            tokens = [token.lemma_ for token in doc
                      if not token.is_punct and not token.is_space and not token.is_stop]
            freq.update(tokens)
        except Exception as e:
            print(f"Error processing line: {line[:30]}... → {e}")

# 上位20単語を表示
for word, count in freq.most_common(20):
    print(f"{word}\t{count}")
