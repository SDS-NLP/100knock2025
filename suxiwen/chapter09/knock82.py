from transformers import BertTokenizer, BertForMaskedLM
import torch
import torch.nn.functional as F

# モデルとトークナイザーの準備
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
model.eval()  # 推論モードに設定

# 入力文
sentence = "The movie was full of [MASK]."
inputs = tokenizer(sentence, return_tensors="pt")

# マスクトークンの位置を特定
mask_token_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]

# モデル推論
with torch.no_grad():
    outputs = model(**inputs)

# マスク位置のロジット（スコア）取得
mask_logits = outputs.logits[0, mask_token_index, :].squeeze()

# softmaxで確率に変換
probs = F.softmax(mask_logits, dim=-1)

# 上位10個の予測トークンとその確率を取得
top_k = 10
top_probs, top_indices = torch.topk(probs, top_k)
top_tokens = tokenizer.convert_ids_to_tokens(top_indices.tolist())

# 結果表示
for i in range(top_k):
    print(f"{i+1}. {top_tokens[i]} - {top_probs[i].item():.4f}")