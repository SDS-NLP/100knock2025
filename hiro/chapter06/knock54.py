import pandas as pd
from gensim.models import KeyedVectors
from tqdm import tqdm
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'GoogleNews-vectors-negative300.bin')
questions_path = os.path.join(script_dir, 'questions-words.txt')

def culcSim(row):
    global model
    return pd.Series(
        list(
            model.most_similar(positive=[row["v2"], row["v3"]], negative=[row["v1"]])[0]
        )
    )

tqdm.pandas()
df = pd.read_csv(questions_path, sep=" ")
df = df.reset_index()
df.columns = ["v1", "v2", "v3", "v4"]
df.dropna(inplace=True)

model = KeyedVectors.load_word2vec_format(model_path, binary=True)
df[["simWord", "simScore"]] = df.progress_apply(culcSim, axis=1)

# 出力ディレクトリを作成
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, "ans54.txt")
df.to_csv(output_path, sep=" ", index=False, header=None)