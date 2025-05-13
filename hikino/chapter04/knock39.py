import re
import MeCab
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


with open("../../../kokoro.txt", "r", encoding="utf-8") as f:
    text = f.read()

chapters = re.split(r'(?=^[一二三四五六七八九十百]+\n)', text, flags=re.MULTILINE)
chapters = [ch.strip() for ch in chapters if ch.strip()]
first = chapters[0]
first = first.replace("\ufeff", "")
chapters[0] = first

chapters = [text.replace("\n", "") for text in chapters]
chapters = [text[1:] for text in chapters]

all_text = ""
for i in range(len(chapters)):
  all_text = all_text + chapters[i]

tagger = MeCab.Tagger("-Owakati -r /etc/mecabrc")
words = tagger.parse(text).strip().split()

counter = Counter(words)
freqs = sorted(counter.values(), reverse=True)
ranks = np.arange(1, len(freqs)+1)

plt.plot(np.log(ranks), np.log(freqs))
plt.xlabel("log(rank)")
plt.ylabel("log(frequency)")
plt.title("Zipf's Law")
plt.savefig("../../../zipf_plot.png")
