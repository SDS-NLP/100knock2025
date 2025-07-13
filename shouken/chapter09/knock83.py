import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

# デバイス設定（GPUあれば使用）
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# モデルとトークナイザの準備
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")
model.to(device)
model.eval()

# 入力文リスト
sentences = [
    "The movie was full of fun.",
    "The movie was full of excitement.",
    "The movie was full of crap.",
    "The movie was full of rubbish."
]

# 各文に対してCLSトークンのベクトルを取得
cls_vectors = []

with torch.no_grad():
    for text in sentences:
        encoded = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        encoded = {k: v.to(device) for k, v in encoded.items()}
        outputs = model(**encoded)
        cls_vec = outputs.last_hidden_state[:, 0, :]  # [CLS]トークンは常に先頭
        cls_vectors.append(cls_vec.cpu().numpy()[0])  # shape: (768,)

# コサイン類似度の計算
similarity_matrix = cosine_similarity(cls_vectors)

# 結果表示
print("コサイン類似度行列：\n")
for i in range(len(sentences)):
    for j in range(len(sentences)):
        print(f"{similarity_matrix[i][j]:.4f}", end="\t")
    print(f"← {sentences[i]}")
