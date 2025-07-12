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

# CLSベクトルを格納するリスト
cls_embeddings = []

# 各文をBERTに通す
with torch.no_grad():
    for sentence in sentences:
        inputs = tokenizer(sentence, return_tensors="pt")
        outputs = model(**inputs)
        # 最終層のCLSベクトルを取り出す
        cls_vector = outputs.last_hidden_state[:, 0, :]
        cls_embeddings.append(cls_vector.squeeze(0))

# 全ペアの組み合わせを取得
pairs = list(itertools.combinations(enumerate(sentences), 2))

# コサイン類似度を計算
for (i, sent1), (j, sent2) in pairs:
    vec1 = cls_embeddings[i]
    vec2 = cls_embeddings[j]
    cosine_sim = F.cosine_similarity(vec1, vec2, dim=0).item()
    print(f"\"{sent1}\"\n  \"{sent2}\" → {cosine_sim:.4f}")

# 結果
"""
"The movie was full of fun."
  "The movie was full of excitement." → 0.9881
"The movie was full of fun."
  "The movie was full of crap." → 0.9558
"The movie was full of fun."
  "The movie was full of rubbish." → 0.9475
"The movie was full of excitement."
  "The movie was full of crap." → 0.9541
"The movie was full of excitement."
  "The movie was full of rubbish." → 0.9487
"The movie was full of crap."
  "The movie was full of rubbish." → 0.9807
"""