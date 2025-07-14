"""
knock84:平均による文ベクトル
以下の文の全ての組み合わせに対して、最終層の埋め込みベクトルの平均を用いて
コサイン類似度を求めよ。
“The movie was full of fun.”
“The movie was full of excitement.”
“The movie was full of crap.”
“The movie was full of rubbish.”
"""
from transformers import BertTokenizer, BertModel
import torch
import torch.nn.functional as F
import itertools

# モデル・トークナイザ読み込み（小文字対応）
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
model.eval()

# 対象文リスト
sentences = [
    "The movie was full of fun.",
    "The movie was full of excitement.",
    "The movie was full of crap.",
    "The movie was full of rubbish."
]

# 各文に対してトークン埋め込みの平均ベクトルを取得
avg_embeddings = []
with torch.no_grad():
    for sentence in sentences:
        inputs = tokenizer(sentence, return_tensors="pt")
        outputs = model(**inputs)
        last_hidden = outputs.last_hidden_state.squeeze(0)  # shape: [seq_len, hidden_size]
        avg_vec = last_hidden.mean(dim=0)  # 各トークン埋め込みの平均
        avg_embeddings.append(avg_vec)

# コサイン類似度を計算（全組み合わせ）
print("Cosine Similarities between MEAN embeddings:\n")
for (i, vec_i), (j, vec_j) in itertools.combinations(enumerate(avg_embeddings), 2):
    sim = F.cosine_similarity(vec_i, vec_j, dim=0).item()
    print(f"{i+1} vs {j+1} : {sim:.4f}")
