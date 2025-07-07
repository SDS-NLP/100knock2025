#82. マスクのtop-k予測
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
mask_logits = logits[0, mask_token_index, :].squeeze()

# top-10トークンとその尤度を取得
top_k = 10
top_k_token_ids = torch.topk(mask_logits, top_k).indices.tolist()

print(f"[MASK] の予測トークン (top-{top_k}):")
for token_id in top_k_token_ids:
    predicted_token = tokenizer.decode([token_id])
    predicted_score = mask_logits[token_id].item()
    print(f"トークン: {predicted_token}, スコア: {predicted_score:.4f}")


