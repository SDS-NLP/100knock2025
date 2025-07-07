#83. CLSトークンによる文ベクトル
from transformers import BertTokenizer, BertModel 
import torch
from sklearn.metrics.pairwise import cosine_similarity

# モデルとトークナイザーの準備
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")
model.eval()

# 対象文
sentences = [
    "The movie was full of fun.",
    "The movie was full of excitement.",
    "The movie was full of crap.",
    "The movie was full of rubbish."
]

# 各文の [CLS] 埋め込みベクトルを取得
cls_embeddings = []

for sentence in sentences:
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    # 隠れ層の先頭にある[CLS]トークンを取得
    cls_vec = outputs.last_hidden_state[:, 0, :]  
    cls_embeddings.append(cls_vec.squeeze(0))     

# ベクトルを1つの行列にまとめる
cls_matrix = torch.stack(cls_embeddings)  # shape: (4, hidden_size)

# コサイン類似度の計算
similarity_matrix = cosine_similarity(cls_matrix.numpy())

# 結果の表示
print("コサイン類似度行列:")
for i in range(len(sentences)):
    for j in range(len(sentences)):
        print(f"({i+1},{j+1}): {similarity_matrix[i][j]:.4f}", end="    ")
    print()
