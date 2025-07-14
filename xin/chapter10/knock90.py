from transformers import GPT2Tokenizer

#token化
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

tokens = tokenizer.tokenize("The movie was full of")
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print(tokens)

from transformers import GPT2LMHeadModel
import torch

model = GPT2LMHeadModel.from_pretrained('gpt2')
input_ids = tokenizer.encode("The movie was full of", return_tensors="pt")
with torch.no_grad():
    outputs = model(input_ids)
    logits = outputs.logits

# 次トークンの予測分布を取得（最後の位置）
next_token_logits = logits[:, -1, :]
probs = torch.softmax(next_token_logits, dim=-1)

# 上位10個のトークンと確率
topk = torch.topk(probs, k=10)
for idx, prob in zip(topk.indices[0], topk.values[0]):
    print(f"{tokenizer.decode(idx.item())} ({prob.item():.5f})")