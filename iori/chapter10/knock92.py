from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# モデルとトークナイザーのロード
model_name = "gpt2"  # 必要に応じて事前学習済みモデルを変更可能
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# 入力テキスト
input_text = "The movie was full of"

# トークン化
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# テキスト生成
output = model.generate(input_ids, max_length=20, num_return_sequences=1, do_sample=True)

# 生成されたテキスト
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated text:", generated_text)

# 各単語の尤度を計算
logits = model(input_ids).logits
log_probs = torch.nn.functional.log_softmax(logits, dim=-1)

# 入力部分のトークンを除外
generated_ids = output[0][len(input_ids[0]):]

print("\nWord probabilities:")
for token_id in generated_ids:
    token_log_prob = log_probs[0, -1, token_id].item()
    word = tokenizer.decode([token_id])
    print(f"Word: {word}, Log Probability: {token_log_prob}")