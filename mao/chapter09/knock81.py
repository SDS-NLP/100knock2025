"""
knock81:マスクの予測
“The movie was full of [MASK].”の”[MASK]”を埋めるのに
最も適切なトークンを求めよ。
"""
from transformers import BertTokenizer, BertForMaskedLM
import torch

# モデルとトークナイザの読み込み
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
model.eval()  # 評価モードに切り替え

# 入力文（[MASK]トークン入り）
text = "The movie was full of [MASK]."
inputs = tokenizer(text, return_tensors="pt")

# モデルで予測
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# [MASK]トークンの位置を取得
mask_token_index = (inputs.input_ids == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]

# 最もスコアの高いトークンを取得
predicted_token_id = logits[0, mask_token_index].argmax(dim=-1)
predicted_token = tokenizer.decode(predicted_token_id)

print("予測トークン:", predicted_token)
