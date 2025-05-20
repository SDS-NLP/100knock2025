import re
from collections import Counter
import pandas as pd

df1 = pd.read_csv("../../../SST-2/dev.tsv", sep="\t")
df2 = pd.read_csv("../../../SST-2/train.tsv", sep="\t")

df1_dct = []
df2_dct = []

def make_list(df, df_dct):
  for i in range(len(df1)):
    sen_dct = {}
    sentence = df.iloc[i, 0]
    label = df.iloc[i, 1]
    sen_dct["text"] = sentence
    sen_dct["label"] = label
    sen_list = re.findall(r'\w+|[^\w\s]', sentence)
    counter = Counter(sen_list)
    counter = dict(counter)
    sen_dct["feature"] = counter
    df_dct.append(sen_dct)

make_list(df1, df1_dct)
make_list(df2, df2_dct)
if __name__ == "__main__":
    print(df1_dct[:5])