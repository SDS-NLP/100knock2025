"""
knock83:CLSトークンによる文ベクトル
以下の文の全ての組み合わせに対して、最終層の[CLS]トークンの埋め込みベクトルを
用いてコサイン類似度を求めよ。
“The movie was full of fun.”
“The movie was full of excitement.”
“The movie was full of crap.”
“The movie was full of rubbish.”
"""
from transformers import BertTokenizer, BertModel
import torch
import torch.nn.functional as F
import itertools

# モデルとトークナイザの準備
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
model.eval()

# 対象文
sentences = [
    "The movie was full of fun.",
    "The movie was full of excitement.",
    "The movie was full of crap.",
    "The movie was full of rubbish."
]

# 各文に対して [CLS] ベクトルを抽出
cls_embeddings = []
with torch.no_grad():
    for sentence in sentences:
        inputs = tokenizer(sentence, return_tensors="pt")
        outputs = model(**inputs)
        cls_vec = outputs.last_hidden_state[:, 0, :]  # [CLS]トークンは先頭
        cls_embeddings.append(cls_vec.squeeze(0))

# 文の組み合わせ全通りに対してコサイン類似度を計算
print("Cosine Similarities between [CLS] embeddings:\n")
for (i, vec_i), (j, vec_j) in itertools.combinations(enumerate(cls_embeddings), 2):
    sim = F.cosine_similarity(vec_i, vec_j, dim=0).item()
    print(f"{i+1} vs {j+1} : {sim:.4f}")
