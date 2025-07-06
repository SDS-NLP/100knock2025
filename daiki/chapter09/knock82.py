from transformers import BertTokenizer, BertForMaskedLM
import torch
import torch.nn.functional as F

# トークナイザとモデルを読み込み
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForMaskedLM.from_pretrained("bert-base-uncased")

# マスク付きの文章
text = "The movie was full of [MASK]."

# トークンIDへ変換
inputs = tokenizer(text, return_tensors="pt")

# モデルに通す
with torch.no_grad():
    outputs = model(**inputs)

# マスクの位置を特定
mask_token_index = (inputs.input_ids == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]

# マスク位置の予測結果（ロジット）
mask_token_logits = outputs.logits[0, mask_token_index, :]

# Softmaxで確率化
probs = F.softmax(mask_token_logits, dim=1)

# 上位10個を取得
top_probs, top_indices = torch.topk(probs, 10, dim=1)

# 表示
for prob, token_id in zip(top_probs[0], top_indices[0]):
    token = tokenizer.decode([token_id]).strip()
    print(f"{token}: {prob.item():.4f}")

# 結果
"""
fun: 0.1071
surprises: 0.0663
drama: 0.0447
stars: 0.0272
laughs: 0.0254
action: 0.0195
excitement: 0.0190
people: 0.0183
tension: 0.0150
music: 0.0146
"""