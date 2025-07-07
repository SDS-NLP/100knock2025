'''
以下の文の全ての組み合わせに対して、最終層の埋め込みベクトルの平均を用いてコサイン類似度を求めよ。

"The movie was full of fun."

"The movie was full of excitement."

"The movie was full of crap."

"The movie was full of rubbish."
'''
from transformers import BertTokenizer, BertModel
import torch
import matplotlib.pyplot as plt
import numpy as np

# 日本語BERTモデルのロード
tokenizer = BertTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
model = BertModel.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')

# 文のリスト
sentences = [
"The movie was full of fun.",
"The movie was full of excitement.",
"The movie was full of crap.",
"The movie was full of rubbish."
]

# 文全体の埋め込みを取得する関数（最終層の埋め込みベクトルの平均）
def get_sentence_embedding(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    
    # 最終層の埋め込みベクトルの平均を返す
    return outputs.last_hidden_state[0].mean(dim=0).detach().numpy()

embeddings = []
for sentence in sentences:
    embedding = get_sentence_embedding(sentence)
    embeddings.append(embedding)

# コサイン類似度の計算
similarities = []
for i in range(len(embeddings)):
    for j in range(i+1, len(embeddings)):
        similarity = np.dot(embeddings[i], embeddings[j]) / (np.linalg.norm(embeddings[i]) * np.linalg.norm(embeddings[j]))
        similarities.append((i, j, similarity))

# 類似度を降順でソート
similarities_sorted = sorted(similarities, key=lambda x: x[2], reverse=True)

print("=== 類似度上位5個 ===")
for i, (idx1, idx2, sim) in enumerate(similarities_sorted[:5], 1):
    print(f"{i}. 類似度: {sim:.4f}")
    print(f"   文1: {sentences[idx1]}")
    print(f"   文2: {sentences[idx2]}")
    print()

print("=== 類似度下位5個 ===")
for i, (idx1, idx2, sim) in enumerate(similarities_sorted[-5:], 1):
    print(f"{i}. 類似度: {sim:.4f}")
    print(f"   文1: {sentences[idx1]}")
    print(f"   文2: {sentences[idx2]}")
    print()
