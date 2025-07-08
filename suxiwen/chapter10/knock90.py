from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# 1. モデルとトークナイザーの読み込み（GPT-2ベースモデル）
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# 2. 入力プロンプトの準備
prompt = "The movie was full of"

# 3. プロンプトのトークン化（トークン列への変換）
inputs = tokenizer(prompt, return_tensors="pt")  # return_tensors="pt"でPyTorchテンソルに変換
input_ids = inputs["input_ids"]  # トークンIDの列（shape: [1, seq_len]）

# 4. トークン列の確認（IDをトークン文字列に変換）
tokens = tokenizer.convert_ids_to_tokens(input_ids[0])  # バッチの0番目を取り出し
print("=== プロンプトのトークン列 ===")
for i, token in enumerate(tokens):
    print(f"トークン{i+1}: {token} (ID: {input_ids[0][i].item()})")

# 5. 次単語予測の実行
with torch.no_grad():  # 勾配計算を無効化（高速化）
    outputs = model(** inputs)  # モデル出力（logitsを含む）

# 6. 次単語のlogitsを抽出（最終位置のlogitsを取得）
next_token_logits = outputs.logits[:, -1, :]  # shape: [1, vocab_size]

# 7. logitsを確率に変換（softmax）
next_token_probs = torch.softmax(next_token_logits, dim=-1).squeeze()  # shape: [vocab_size]

# 8. 上位10個のトークンと確率を抽出
top_k = 10
top_probs, top_indices = torch.topk(next_token_probs, top_k)

# 9. 結果の表示
print("\n=== 上位10個の次トークンと確率 ===")
for i in range(top_k):
    token_id = top_indices[i].item()
    token = tokenizer.convert_ids_to_tokens(token_id)
    prob = top_probs[i].item() * 100  # パーセント表示
    print(f"{i+1}. トークン: {token} | 確率: {prob:.2f}%")