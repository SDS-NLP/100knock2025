from gensim.models import KeyedVectors
from knock50 import model

similar_words = model.most_similar("United_States", topn=10)

# 結果を表示
for word, similarity in similar_words:
    print(f"{word}->{similarity:.4f}")
