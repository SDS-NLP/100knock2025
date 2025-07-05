#84. 平均による文ベクトル
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

# 各文の埋め込みベクトルを取得
embeddings = []

for sentence in sentences:
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    # 最終層のトークン埋め込み (batch=1, seq_len, hidden_size)
    token_embeddings = outputs.last_hidden_state.squeeze(0)  
    # 平均プーリング（全トークンのベクトル平均）
    sentence_embedding = token_embeddings.mean(dim=0)     
    embeddings.append(sentence_embedding)   

# ベクトルを1つの行列にまとめる
cls_matrix = torch.stack(embeddings)  

# コサイン類似度の計算
similarity_matrix = cosine_similarity(cls_matrix.numpy())

# 結果の表示
print("コサイン類似度行列:")
for i in range(len(sentences)):
    for j in range(len(sentences)):
        print(f"({i+1},{j+1}): {similarity_matrix[i][j]:.4f}", end="    ")
    print()

#83よりも正確？