from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import torch.nn.functional as F

# モデルとトークナイザのロード
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# プロンプト
prompt = "The movie was full of"
input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

# テキストを適度な長さ（例: 10トークン）で生成
max_new_tokens = 10
output_ids = model.generate(
    input_ids,
    max_new_tokens=max_new_tokens,
    do_sample=False,  # greedy
)
# 出力トークン全体
all_ids = output_ids[0]

# 各トークンの尤度（log-prob）を計算
with torch.no_grad():
    outputs = model(all_ids[:-1].unsqueeze(0))
    logits = outputs.logits
    probs = F.log_softmax(logits, dim=-1)  # log-prob
    log_probs = probs[0, torch.arange(len(all_ids)-1), all_ids[1:]]  # 次トークンの対数確率

# トークンごとの表示
print(f"\nPrompt: {prompt}\n")
for i in range(len(input_ids[0]), len(all_ids)):
    token = tokenizer.decode([all_ids[i]])
    log_prob = log_probs[i - len(input_ids[0])].item()
    print(f"Generated token: {token!r:>12} | Log-Prob: {log_prob:>8.4f}")
