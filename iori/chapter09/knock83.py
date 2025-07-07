from itertools import combinations
from transformers import BertTokenizer, BertModel
import torch

import torch.nn.functional as F

# 文のリスト
sentences = [
    "The movie was full of fun.",
    "The movie was full of excitement.",
    "The movie was full of crap.",
    "The movie was full of rubbish."
]

# BERTモデルとトークナイザーのロード
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# 文の埋め込みベクトルを取得
def get_cls_embedding(sentence):
    inputs = tokenizer(sentence, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    # [CLS]トークンの埋め込みベクトルを取得
    cls_embedding = outputs.last_hidden_state[:, 0, :]
    return cls_embedding

# コサイン類似度を計算
def cosine_similarity(vec1, vec2):
    return F.cosine_similarity(vec1, vec2).item()

# 全ての文の組み合わせに対してコサイン類似度を計算
for (sent1, sent2) in combinations(sentences, 2):
    vec1 = get_cls_embedding(sent1)
    vec2 = get_cls_embedding(sent2)
    similarity = cosine_similarity(vec1, vec2)
    print(f"Cosine similarity between:\n'{sent1}'\nand\n'{sent2}'\n=> {similarity:.4f}\n")