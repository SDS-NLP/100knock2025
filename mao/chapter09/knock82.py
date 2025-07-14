"""
knock82:マスクのtop-k予測
“The movie was full of [MASK].”の”[MASK]”に埋めるのに
適切なトークン上位10個と、その確率（尤度）を求めよ。
"""
from transformers import BertTokenizer, BertForMaskedLM
import torch
import torch.nn.functional as F

# モデルとトークナイザを読み込み
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
model.eval()

# 入力文
text = "The movie was full of [MASK]."
inputs = tokenizer(text, return_tensors="pt")

# モデル出力取得
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# [MASK]の位置特定
mask_token_index = (inputs.input_ids == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]

# 対象位置のロジットを softmax で確率に変換
mask_logits = logits[0, mask_token_index, :]
probs = F.softmax(mask_logits, dim=-1)

# 上位10件を抽出
top_k = 10
top_probs, top_indices = torch.topk(probs, top_k, dim=-1)

# 結果表示
print("Top 10 predictions for [MASK]:")
for i in range(top_k):
    token = tokenizer.decode(top_indices[0, i])
    prob = top_probs[0, i].item()
    print(f"{i+1:2d}: {token:<15} ({prob:.4f})")
