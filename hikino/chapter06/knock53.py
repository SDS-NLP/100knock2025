from gensim.models import KeyedVectors
from knock50 import model

result = model.most_similar(positive=["Spain", "Athens"], negative=["Madrid"], topn=10)

for word, similarity in result:
    print(f"{word}->{similarity:.4f}")
