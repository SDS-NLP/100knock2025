from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import torch.nn.functional as F

# モデルとトークナイザーの読み込み
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

# 入力文
prompt = "The movie was full of"

# トークン化（どのトークン列に変換されたか確認）
inputs = tokenizer(prompt, return_tensors="pt")
input_ids = inputs["input_ids"]
print("Input tokens:", tokenizer.convert_ids_to_tokens(input_ids[0]))

# モデルに通す
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits  # shape: [1, seq_len, vocab_size]

# 最後のトークン位置でのlogitsを取得（次トークンの予測）
next_token_logits = logits[0, -1, :]  # shape: [vocab_size]

# softmaxで確率化
probs = F.softmax(next_token_logits, dim=-1)

# 上位10個を取得
topk = 10
topk_probs, topk_indices = torch.topk(probs, topk)

# 結果表示
print("\nTop 10 next token predictions:")
for i in range(topk):
    token = tokenizer.decode([topk_indices[i]])
    prob = topk_probs[i].item()
    print(f"{i+1}. {token!r:15s} (probability: {prob:.5f})")
