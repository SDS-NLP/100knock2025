from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import torch.nn.functional as F

# モデルとトークナイザ読み込み
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# プロンプト
prompt = "The movie was full of"

# トークナイズ
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# テキスト生成
# do_sample=True → ランダム性を持たせる
# max_new_tokens → 生成するトークン数
generated_ids = model.generate(
    input_ids,
    max_new_tokens=10,
    do_sample=True,
    temperature=1.0
)

# 生成された全ID列
# 例: [The, movie, was, full, of, ..., 新規トークンたち]
all_ids = generated_ids[0]

# 確率を計算するため
# すべてのトークンの logits を取得
with torch.no_grad():
    outputs = model(all_ids.unsqueeze(0))
    logits = outputs.logits

# 確率計算
# logits[i] は i 番目の token を予測するための確率分布
# → つまり token[i] を予測する確率は logits[i-1] から取り出す

tokens = tokenizer.convert_ids_to_tokens(all_ids)
probs_list = []

for i in range(len(all_ids)):
    if i == 0:
        # 最初の token は文脈なしなのでスキップ
        probs_list.append(None)
        continue

    # 前の位置の logits からソフトマックスを計算
    prev_logits = logits[0, i-1]
    probs = F.softmax(prev_logits, dim=-1)

    # 今のトークンの id の確率を取り出す
    token_id = all_ids[i].item()
    token_prob = probs[token_id].item()

    probs_list.append(token_prob)

# 表示
print("Generated Text and Token Probabilities")
for token, prob in zip(tokens, probs_list):
    if prob is None:
        print(f"{token}\t-")
    else:
        print(f"{token}\t{prob:.5f}")

# 最終的な生成結果
decoded_text = tokenizer.decode(all_ids, skip_special_tokens=True)
print("\nGenerated text:", decoded_text)

# 出力結果
"""
Generated text: The movie was full of interesting characters and some of us were very surprised and
Ġinteresting    0.00442
Ġcharacters     0.11221
Ġand    0.23735
Ġsome   0.03905
Ġof     0.08346
Ġus     0.00308
Ġwere   0.16671
Ġvery   0.03499
Ġsurprised      0.04927
Ġand    0.05263
"""