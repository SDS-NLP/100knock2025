import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

# モデル準備
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

# 対象文
sentences = [
    "The movie was full of fun.",
    "The movie was full of excitement.",
    "The movie was full of crap.",
    "The movie was full of rubbish."
]

# 文ごとに平均ベクトルを取得
avg_vectors = []

with torch.no_grad():
    for text in sentences:
        encoded = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        encoded = {k: v.to(device) for k, v in encoded.items()}
        outputs = model(**encoded)
        token_embeddings = outputs.last_hidden_state  # (1, seq_len, hidden_dim)
        mean_vec = token_embeddings.mean(dim=1)       # 平均 (1, hidden_dim)
        avg_vectors.append(mean_vec.cpu().numpy()[0]) # shape: (768,)

# コサイン類似度行列
similarity_matrix = cosine_similarity(avg_vectors)

# 結果表示
print("コサイン類似度行列（平均ベクトル使用）:\n")
for i in range(len(sentences)):
    for j in range(len(sentences)):
        print(f"{similarity_matrix[i][j]:.4f}", end="\t")
    print(f"← {sentences[i]}")
