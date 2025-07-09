from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import torch.nn.functional as F

# モデルとトークナイザー
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval().cuda()

# 入力プロンプト
prompt = "The movie was full of"
input_ids = tokenizer.encode(prompt, return_tensors='pt').cuda()

# テキストを続き10トークン生成（samplingで自然な文を作る）
with torch.no_grad():
    output_ids = model.generate(
        input_ids,
        max_new_tokens=10,
        do_sample=True,
        temperature=1.0,
        pad_token_id=tokenizer.eos_token_id  # avoid warning
    )

# 生成されたすべてのトークン列
all_tokens = output_ids[0]
decoded_text = tokenizer.decode(all_tokens)
print("=== 生成結果 ===")
print(decoded_text)

# 尤度を計算するために logits を再取得
with torch.no_grad():
    outputs = model(output_ids)
    logits = outputs.logits  # [1, seq_len, vocab_size]

# softmaxで確率を得る
probs = F.softmax(logits, dim=-1)

# 各トークンの尤度（次トークンの予測確率）
print("\n=== 各トークンの尤度 ===")
for i in range(1, len(all_tokens)):
    prev_token = all_tokens[i - 1].item()
    current_token = all_tokens[i].item()
    token_str = tokenizer.decode([current_token])
    prob = probs[0, i - 1, current_token].item()
    print(f"{i:02d}: '{token_str}' (P={prob:.5f})")
