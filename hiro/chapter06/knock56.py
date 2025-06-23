import pandas as pd
import os
from gensim.models import KeyedVectors
from tqdm import tqdm


def culcCosSim(row):
    global model
    return model.similarity(row["Word 1"], row["Word 2"])


tqdm.pandas()
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'GoogleNews-vectors-negative300.bin')
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
csv_path = os.path.join(script_dir, 'wordsim353', 'combined.csv')
df = pd.read_csv(csv_path)
df["cosSim"] = df.progress_apply(culcCosSim, axis=1)

print(df[["Human (mean)", "cosSim"]].corr(method="spearman"))