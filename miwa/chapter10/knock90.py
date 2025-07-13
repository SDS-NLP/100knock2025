#90. 次単語予測
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import torch.nn.functional as F

# モデルとトークナイザーの読み込み
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

# 入力プロンプト
text = "The movie was full of"
input_ids = tokenizer.encode(text, return_tensors="pt")

# トークン列を確認
tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
print("入力テキストのトークン列:", tokens)

# モデルによる予測
with torch.no_grad():
    outputs = model(input_ids)
    logits = outputs.logits  # (batch_size, sequence_length, vocab_size)

# 最後の位置のロジット（次トークンの予測に相当）
next_token_logits = logits[0, -1, :]

# 確率（softmax）
probs = F.softmax(next_token_logits, dim=-1)

# 上位10トークンとその確率を取得
topk = torch.topk(probs, k=10)
topk_tokens = topk.indices
topk_probs = topk.values

print("次に来る可能性の高いトークン（Top 10）:")
for i, (token_id, prob) in enumerate(zip(topk_tokens, topk_probs)):
    token_str = tokenizer.decode(token_id.item())
    print(f"{i+1}. '{token_str}'  - 確率: {prob.item():.5f}")
