from transformers import BertTokenizer, BertForMaskedLM
import torch

# トークナイザとモデルを読み込む
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

# 最上位トークンを取得
top_tokens = torch.topk(mask_token_logits, 1, dim=1).indices[0].tolist()

# トークンを文字列に変換して表示
for token_id in top_tokens:
    token = tokenizer.decode([token_id]).strip()
    print(token)

# 結果
"""
fun
"""