from transformers import BertTokenizer, BertForMaskedLM
import torch

# モデルとトークナイザーの準備
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')

# 入力文（MASK付き）
sentence = "The movie was full of [MASK]."
inputs = tokenizer(sentence, return_tensors="pt")

# マスク位置の取得
mask_token_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]

# 予測
with torch.no_grad():
    outputs = model(**inputs)

# ログ確率上位のトークン候補
logits = outputs.logits
mask_token_logits = logits[0, mask_token_index, :]
top_tokens = torch.topk(mask_token_logits, 5, dim=1).indices[0].tolist()

# トークンを人間が読める形に
predicted_words = tokenizer.convert_ids_to_tokens(top_tokens)
print(predicted_words)