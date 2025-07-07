from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# モデル・トークナイザーの準備
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")
model.eval()

# 対象の文
sentences = [
    "The movie was full of fun.",
    "The movie was full of excitement.",
    "The movie was full of crap.",
    "The movie was full of rubbish."
]

# CLSベクトルを取得する関数
def get_cls_embedding(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    # 最終層のCLS（位置0）の出力
    cls_embedding = outputs.last_hidden_state[0, 0, :]  # shape: [hidden_size]
    return cls_embedding

# 全文のCLSベクトルを取得
cls_embeddings = [get_cls_embedding(s).numpy() for s in sentences]

# コサイン類似度行列を計算
similarity_matrix = cosine_similarity(cls_embeddings)

# 結果を表示
import pandas as pd
df = pd.DataFrame(similarity_matrix, index=sentences, columns=sentences)
print(df)
