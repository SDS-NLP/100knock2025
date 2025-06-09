import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from gensim.models import KeyedVectors
from sklearn.manifold import TSNE

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "questions-words.txt")
df = pd.read_csv(csv_path, sep=" ")
df = df.reset_index()
df.columns = ["v1", "v2", "v3", "v4"]
df.dropna(inplace=True)
df = df.iloc[:5030]
country = list(set(df["v4"].values))

model_path = os.path.join(script_dir, 'GoogleNews-vectors-negative300.bin')
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

countryVec = []
for c in country:
    countryVec.append(model[c])

X = np.array(countryVec)
tsne = TSNE(random_state=0, n_iter=15000, metric="cosine")
embs = tsne.fit_transform(X)
plt.scatter(embs[:, 0], embs[:, 1])
plt.show()