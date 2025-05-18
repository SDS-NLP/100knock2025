from knock62 import model, vectorizer
import re
from collections import Counter

new_text = "the worst movie I 've ever seen"
sen_list = re.findall(r'\w+|[^\w\s]', new_text)
counter = Counter(sen_list)
counter = dict(counter)

X_new = vectorizer.transform([counter])

pred = model.predict(X_new)
print("予測ラベル:", pred[0])
