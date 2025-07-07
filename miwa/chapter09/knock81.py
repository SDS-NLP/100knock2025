#81. マスクの予測
from transformers import BertTokenizer, BertForMaskedLM
import torch

# モデルとトークナイザーの準備（小文字化あり）
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForMaskedLM.from_pretrained("bert-base-uncased")
model.eval()

# 対象文
sentence = "The movie was full of [MASK]."

# トークン化 + テンソル化
inputs = tokenizer(sentence, return_tensors="pt")

# マスクの位置を特定
mask_token_index = (inputs["input_ids"] == tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]

# 予測
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# マスク位置の予測スコアを取得
mask_logits = logits[0, mask_token_index, :]

# 最もスコアの高いトークンを取得
top_token_id = torch.argmax(mask_logits, dim=-1).item()
predicted_token = tokenizer.decode([top_token_id])

print(f"[MASK] の予測トークン: {predicted_token}")


