from transformers import BertTokenizer, BertForMaskedLM
import torch

# モデルとトークナイザーの準備
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForMaskedLM.from_pretrained("bert-base-uncased")
model.eval()

# マスク入りの文
sentence = "The movie was full of [MASK]."
inputs = tokenizer(sentence, return_tensors="pt")

# モデルに入力して予測を取得
with torch.no_grad():
    outputs = model(**inputs)
    predictions = outputs.logits

# [MASK]の位置を特定し、最も確率の高い単語を選ぶ
mask_token_index = (inputs.input_ids == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]
mask_token_logits = predictions[0, mask_token_index, :]
top_token_id = torch.argmax(mask_token_logits, dim=-1)
predicted_token = tokenizer.decode(top_token_id)

print("Predicted token:", predicted_token)
