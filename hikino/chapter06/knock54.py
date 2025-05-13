from gensim.models import KeyedVectors
from knock50 import model

results = []
right_answer = []

with open("../../../questions-words.txt", "r", encoding="utf-8") as f:
    capture = False
    for line in f:
        if line.startswith(":"):
            capture = (line.strip() == ": capital-common-countries")
            continue
        if not capture:
            continue

        w1, w2, w3, w4 = line.strip().split()
        right_answer.append(w4)

        if all(word in model for word in (w1, w2, w3)):
            predicted = model.most_similar(positive=[w2, w3], negative=[w1], topn=1)[0]
            predicted_word, similarity = predicted
            results.append((w1, w2, w3, predicted_word, similarity))

if __name__ == "__main__":
  for r in results[:5]:
    print(f"{r[0]}:{r[1]}::{r[2]}:? => {r[3]} ({r[4]:.4f})")
