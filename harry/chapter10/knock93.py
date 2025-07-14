# knock93.py
# 目的: 複数の文に対してGPT2でパープレキシティを計算・比較する

import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import math

# モデルとトークナイザーの読み込み
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# GPUが使えれば使う
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 評価したい文のリスト（文法的に正しいもの・間違っているものを含む）
sentences = [
    "The movie was full of surprises",   # ✅ 正しい
    "The movies were full of surprises", # ✅ 正しい
    "The movie were full of surprises",  # ❌ 間違い
    "The movies was full of surprises"   # ❌ 間違い
]

# パープレキシティを計算する関数
def calculate_perplexity(sentence):
    # トークン化してテンソルに変換
    inputs = tokenizer(sentence, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)

    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        # 平均クロスエントロピーロスを取得
        loss = outputs.loss
        # パープレキシティ = exp(平均損失)
        perplexity = math.exp(loss.item())
        return perplexity

# 各文のパープレキシティを表示
print("📊 パープレキシティ結果（小さいほど自然）:")
for sent in sentences:
    ppl = calculate_perplexity(sent)
    print(f"・\"{sent}\" → PPL: {ppl:.4f}")
