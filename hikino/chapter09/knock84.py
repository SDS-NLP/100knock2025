from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# モデルとトークナイザーの読み込み
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")
model.eval()

# 文リスト
sentences = [
    "The movie was full of fun.",
    "The movie was full of excitement.",
    "The movie was full of crap.",
    "The movie was full of rubbish."
]

# トークン全体のベクトルの平均を取る関数
def get_mean_embedding(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    last_hidden_state = outputs.last_hidden_state  # shape: [1, seq_len, hidden_size]
    mean_vector = last_hidden_state.mean(dim=1).squeeze()  # 平均: shape [hidden_size]
    return mean_vector.numpy()

# 全文に対して平均ベクトルを取得
mean_embeddings = [get_mean_embedding(s) for s in sentences]

# コサイン類似度行列の作成
similarity_matrix = cosine_similarity(mean_embeddings)

# DataFrameで表示
df = pd.DataFrame(similarity_matrix, index=sentences, columns=sentences)
print(df)
