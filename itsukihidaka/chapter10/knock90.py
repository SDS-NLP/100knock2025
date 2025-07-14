from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import torch.nn.functional as F

# モデルとトークナイザーのロード
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# 入力文
input_text = "The movie was full of"
inputs = tokenizer(input_text, return_tensors="pt")

# トークナイズされたトークン列を表示
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
print("Tokenized Input:")
print(tokens)

# モデルで予測（logits を得る）
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# 最後のトークン位置の出力から次トークンの確率分布を得る
last_token_logits = logits[0, -1, :]
print('last_token_logits', last_token_logits)
probs = F.softmax(last_token_logits, dim=-1)
print('probs', probs)

# Top-k（上位10個）のトークンと確率を取得
top_k = 10
top_probs, top_indices = torch.topk(probs, top_k)
print('top_probs', top_probs)
print('top_indices', top_indices)
print("\nTop 10 next token predictions:")
for i in range(top_k):
    token = tokenizer.decode([top_indices[i].item()])
    prob = top_probs[i].item()
    print(f"{i+1}: '{token}' (probability: {prob:.5f})")
