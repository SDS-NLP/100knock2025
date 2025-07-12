# knock92.py
# 目的: GPT2で生成された各単語の尤度（確率）を表示（sampling + temperature指定）

import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch.nn.functional as F

# モデルとトークナイザーの読み込み
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# プロンプト
prompt = "The movie was full of"

# トークン化とattention maskの作成
inputs = tokenizer(prompt, return_tensors="pt")
input_ids = inputs.input_ids
attention_mask = inputs.attention_mask

# max_new_tokens=10で短めに生成（sampling使用）
with torch.no_grad():
    output_ids = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_new_tokens=10,
        do_sample=True,              # 🔸 samplingを有効にする
        temperature=0.7,             # 🔸 温度パラメータ指定
        top_k=50,                    # 🔸 top-k制限（多様性向上）
        top_p=0.95,                  # 🔸 nucleus sampling
        return_dict_in_generate=True,
        output_scores=True,
        pad_token_id=tokenizer.eos_token_id
    )

# 出力トークン列（生成部分のみ）
generated_ids = output_ids.sequences[0]
generated_tokens = generated_ids[len(input_ids[0]):]

# 各トークンのlogitsからsoftmaxで確率を計算
scores = output_ids.scores
probs_list = [F.softmax(score, dim=-1) for score in scores]

# 表示
print(f"\n📝 プロンプト: {prompt}")
print("🔮 生成されたテキスト:")
print(tokenizer.decode(generated_ids, skip_special_tokens=True))

print("\n📊 各生成トークンとその尤度（確率）:")
for token_id, probs in zip(generated_tokens, probs_list):
    token = tokenizer.decode(token_id)
    prob = probs[0, token_id].item()  # 🔸 バッチ次元に注意
    print(f"・'{token}': {prob:.6f}")
