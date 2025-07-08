from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# モデルとトークナイザーのロード
model_name = "gpt2"  # 必要に応じて事前学習済みモデルを変更可能
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# プロンプトの設定
prompt = "The movie was full of"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# トークン列の確認
decoded_prompt = tokenizer.decode(input_ids[0])
print(f"Tokenized prompt: {decoded_prompt}")

# 次のトークンの予測
with torch.no_grad():
    outputs = model(input_ids)
    logits = outputs.logits

# ソフトマックスで確率を計算
next_token_logits = logits[0, -1, :]
probabilities = torch.softmax(next_token_logits, dim=-1)

# 上位10個のトークンと確率を取得
top_k = 10
top_k_indices = torch.topk(probabilities, top_k).indices
top_k_probs = torch.topk(probabilities, top_k).values

# 結果の表示
print("\nTop 10 predictions:")
for i, (token_id, prob) in enumerate(zip(top_k_indices, top_k_probs)):
    token = tokenizer.decode([token_id])
    print(f"{i+1}: {token} (Probability: {prob.item():.6f})")