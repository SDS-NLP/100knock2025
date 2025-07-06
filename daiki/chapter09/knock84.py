from transformers import BertTokenizer, BertModel
import torch
import itertools
import torch.nn.functional as F

# 文リスト
sentences = [
    "The movie was full of fun.",
    "The movie was full of excitement.",
    "The movie was full of crap.",
    "The movie was full of rubbish."
]

# トークナイザとモデルを読み込み
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# 平均ベクトルを格納するリスト
avg_embeddings = []

# 各文をBERTに通す
with torch.no_grad():
    for sentence in sentences:
        inputs = tokenizer(sentence, return_tensors="pt")
        outputs = model(**inputs)
        # 全トークンの埋め込みを取得
        all_tokens = outputs.last_hidden_state[0]  # shape: [seq_len, hidden_size]
        avg_vector = all_tokens.mean(dim=0)        # 平均を計算
        avg_embeddings.append(avg_vector)

# 全ペアの組み合わせを取得
pairs = list(itertools.combinations(enumerate(sentences), 2))

# コサイン類似度を計算
for (i, sent1), (j, sent2) in pairs:
    vec1 = avg_embeddings[i]
    vec2 = avg_embeddings[j]
    cosine_sim = F.cosine_similarity(vec1, vec2, dim=0).item()
    print(f"\"{sent1}\"\n  \"{sent2}\" → {cosine_sim:.4f}")

# 結果
"""
"The movie was full of fun."
  "The movie was full of excitement." → 0.9568
"The movie was full of fun."
  "The movie was full of crap." → 0.8490
"The movie was full of fun."
  "The movie was full of rubbish." → 0.8169
"The movie was full of excitement."
  "The movie was full of crap." → 0.8352
"The movie was full of excitement."
  "The movie was full of rubbish." → 0.7938
"The movie was full of crap."
  "The movie was full of rubbish." → 0.9226
"""