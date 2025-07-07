from transformers import BertTokenizer, BertModel
import torch
import torch.nn.functional as F
import itertools
import pandas as pd

# モデルとトークナイザーの用意
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
model.eval()

# 文リスト
sentences = [
    "The movie was full of fun.",
    "The movie was full of excitement.",
    "The movie was full of crap.",
    "The movie was full of rubbish."
]

# CLSベクトルの抽出
cls_embeddings = []
for sentence in sentences:
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    cls_vector = outputs.last_hidden_state[0, 0]  # [CLS] トークンのベクトル
    cls_embeddings.append(cls_vector)

# コサイン類似度の計算
similarity_matrix = []
for vec1 in cls_embeddings:
    row = []
    for vec2 in cls_embeddings:
        sim = F.cosine_similarity(vec1.unsqueeze(0), vec2.unsqueeze(0)).item()
        row.append(round(sim, 4))
    similarity_matrix.append(row)

# 表示用データフレーム
df = pd.DataFrame(similarity_matrix, columns=sentences,index=sentences)
print(df)