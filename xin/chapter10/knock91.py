from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# モデルとトークナイザのロード
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# GPUが使えればGPUへ移動
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# 入力テキスト
prompt = "The movie was full of"
input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

# デコーディング戦略の設定と結果表示
def generate_with_settings(strategy, temperature=1.0, top_k=0, top_p=1.0):
    print(f"\n--- {strategy} (temperature={temperature}, top_k={top_k}, top_p={top_p}) ---")
    output = model.generate(
        input_ids,
        max_length=30,
        do_sample=(strategy != "greedy"),
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        num_return_sequences=3,  # 複数出力
    )
    for i, sequence in enumerate(output):
        print(f"[{i+1}] {tokenizer.decode(sequence, skip_special_tokens=True)}")

# 各設定で生成
generate_with_settings("greedy")  # Greedy search
generate_with_settings("sampling", temperature=1.0)
generate_with_settings("sampling", temperature=1.5)
generate_with_settings("top-k", temperature=1.0, top_k=50)
generate_with_settings("top-p", temperature=1.0, top_p=0.9)
