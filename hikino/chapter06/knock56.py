import pandas as pd
from gensim.models import KeyedVectors
from scipy.stats import spearmanr
from knock50 import model

df = pd.read_csv("../../../combined.csv") 
df.columns = ["Word1", "Word2", "Human"]

predicted_sim = []
human_sim = []

for _, row in df.iterrows():
    w1, w2 = row["Word1"], row["Word2"]
    if w1 in model and w2 in model:
        sim = model.similarity(w1, w2)
        predicted_sim.append(sim)
        human_sim.append(row["Human"])

correlation, _ = spearmanr(predicted_sim, human_sim)
print(f"Spearman correlation: {correlation:.4f}")
