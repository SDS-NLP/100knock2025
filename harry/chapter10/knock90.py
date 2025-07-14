# knock90.py
# 目的: GPT2モデルで「The movie was full of」の次のトークンを予測し、上位10個とその確率を表示する

import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch.nn.functional as F

# モデル名（小さいGPT2モデル）
MODEL_NAME = 'gpt2'

# トークナイザーとモデルを読み込む（事前学習済みのもの）
tokenizer = GPT2Tokenizer.from_pretrained(MODEL_NAME)
model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
model.eval()  # 評価モードにする（学習ではなく推論）

# 入力文
prompt = "The movie was full of"

# 入力文をトークン化（ID列に変換）＋tensor化（モデルで扱える形式）
inputs = tokenizer(prompt, return_tensors="pt")

# モデルに入力し、出力を得る（logits: 各トークンに対するスコア）
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# 最後の位置のトークンに対応するlogitsを取り出す
last_token_logits = logits[0, -1]  # 形状: [vocab_size]

# softmaxで確率に変換
probs = F.softmax(last_token_logits, dim=-1)

# 上位10個のスコアが高いトークンのインデックスを取得
top_k = 10
top_probs, top_indices = torch.topk(probs, top_k)

# トークンIDを文字に戻す
top_tokens = [tokenizer.decode([idx]) for idx in top_indices]

# 結果を表示
print("📝 プロンプト:", prompt)
print("\n🧾 トークン化されたID列:", inputs['input_ids'][0].tolist())
print("🧾 トークン列:", [tokenizer.decode([tid]) for tid in inputs['input_ids'][0]])

print("\n🔮 次に続く可能性の高いトークン（Top 10）:")
for token, prob in zip(top_tokens, top_probs):
    print(f"・'{token}': {prob.item():.4f}")
