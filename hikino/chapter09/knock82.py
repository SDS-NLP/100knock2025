from transformers import BertTokenizer, BertForMaskedLM
import torch
import torch.nn.functional as F

# モデルとトークナイザーの準備
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForMaskedLM.from_pretrained("bert-base-uncased")
model.eval()

# 入力文
sentence = "The movie was full of [MASK]."
inputs = tokenizer(sentence, return_tensors="pt")

# モデルに通して予測を得る
with torch.no_grad():
    outputs = model(**inputs)
    predictions = outputs.logits

# [MASK] の位置を特定
mask_token_index = (inputs.input_ids == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]
mask_token_logits = predictions[0, mask_token_index, :].squeeze()

# softmaxで確率に変換
probabilities = F.softmax(mask_token_logits, dim=-1)

# 上位10個を取得
topk = 10
topk_probs, topk_indices = torch.topk(probabilities, topk)

# トークンと確率を表示
for i in range(topk):
    token = tokenizer.decode([topk_indices[i]])
    prob = topk_probs[i].item()
    print(f"{i+1}. {token:15} (probability: {prob:.5f})")
