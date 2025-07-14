"""
knock92:予測されたテキストの確率を計算
“The movie was full of”に続くテキストを予測し、
生成された各単語の尤度を表示せよ
（生成されるテキストが長いと出力が読みにくくなるので、
適当な長さで生成を打ち切るとよい）。
"""
#GPUじゃないと動かなさそう
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import torch.nn.functional as F

# モデルとトークナイザの準備
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 入力
prompt = "The movie was full of"
max_new_tokens = 20

# 入力トークナイズ＋attention_mask明示
input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
attention_mask = torch.ones_like(input_ids).to(device)

# 生成 + 出力スコア取得
outputs = model.generate(
    input_ids,
    attention_mask=attention_mask,
    max_new_tokens=max_new_tokens,
    return_dict_in_generate=True,
    output_scores=True,
    do_sample=False,  # Greedy decoding
    pad_token_id=tokenizer.eos_token_id
)

# 生成されたID列（input + output）
generated_ids = outputs.sequences[0]

# 各タイムステップの確率
logits = torch.stack(outputs.scores, dim=0)
probs = F.softmax(logits, dim=-1)

# トークンごとの確率を表示
print(f"📝 入力文: {prompt}")
print("📈 生成トークンとその尤度（確率）:")
for i in range(max_new_tokens):
    token_id = generated_ids[input_ids.shape[1] + i].item()
    token = tokenizer.decode([token_id])
    prob = probs[i, token_id].item()
    print(f"{i+1:2d}. '{token.strip()}': 確率 = {prob:.5f}")
