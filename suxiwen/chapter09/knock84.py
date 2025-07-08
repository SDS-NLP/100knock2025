from transformers import BertTokenizer, BertModel
import torch
import torch.nn.functional as F
import pandas as pd

# モデルとトークナイザーの用意
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

# ベクトル格納リスト
mean_embeddings = []

# 各文に対する平均ベクトルを取得
for sentence in sentences:
    inputs = tokenizer(sentence, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)

    # トークンの隠れ状態（[batch, seq_len, hidden]）
    hidden_states = outputs.last_hidden_state.squeeze(0)  # [seq_len, hidden]
    attention_mask = inputs['attention_mask'].squeeze(0).unsqueeze(-1)  # [seq_len, 1]

    # attention maskを使ってパディングを除外した平均
    masked_hidden = hidden_states * attention_mask
    mean_vec = masked_hidden.sum(dim=0) / attention_mask.sum()
    mean_embeddings.append(mean_vec)

# コサイン類似度行列を計算
similarity_matrix = []
for vec1 in mean_embeddings:
    row = []
    for vec2 in mean_embeddings:
        similarity = F.cosine_similarity(vec1.unsqueeze(0), vec2.unsqueeze(0)).item()
        row.append(round(similarity, 4))
    similarity_matrix.append(row)

# 表示用にDataFrame化
df = pd.DataFrame(similarity_matrix, columns=sentences, index=sentences)
print(df)