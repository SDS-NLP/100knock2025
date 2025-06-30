from knock62 import model, vectorizer
import re
from collections import Counter

text = "the worst movie I 've ever seen"
word = re.findall(r'\w+|[^\w\s]', text)
counter = dict(Counter(word))

vec = vectorizer.transform([counter])

pred = model.predict(vec)
print("予測ラベル:", pred[0])