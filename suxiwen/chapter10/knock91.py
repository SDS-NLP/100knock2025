from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# 1. モデルとトークナイザーの読み込み（GPT-2を使用）
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# GPT-2にはデフォルトでpad_tokenがないため、eos_tokenをpad_tokenとして設定
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()  # 評価モードに設定（ドロップアウト等を無効化）

# 2. 入力プロンプトの準備
prompt = "The movie was full of"
inputs = tokenizer(prompt, return_tensors="pt")
input_ids = inputs["input_ids"]

# 3. デコーディングパラメータの設定（複数条件を比較）
# 条件: (デコーディング方法, 温度, 生成最大長)
decoding_params = [
    ("贪心搜索 (Greedy)", 1.0, 50),
    ("Beam Search (k=3)", 1.0, 50),
    ("采样 (Sampling)", 0.3, 50),  # 低温度：結果が安定
    ("采样 (Sampling)", 1.5, 50),  # 高温度：結果が多様
    ("采样+Top-K=10", 1.0, 50),    # Top-K制約付き采样
]

# 4. テキスト生成と結果表示
print(f"=== 入力プロンプト: {prompt} ===")
for method, temp, max_len in decoding_params:
    print(f"\n--- デコーディング方法: {method} | 温度: {temp} ---")
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=len(input_ids[0]) + max_len,  # 入力長 + 生成長
            temperature=temp,                        # 温度パラメータ
            do_sample=(method != "贪心搜索 (Greedy)"),  # 采样モード（贪心搜索時はFalse）
            num_beams=3 if "Beam" in method else 1,  # Beam Searchの場合k=3
            top_k=10 if "Top-K=10" in method else 500,  # Top-K制約
            early_stopping=True,                     # 終了トークン出現時に生成停止
            pad_token_id=tokenizer.pad_token_id,     # パディングトークン指定
            eos_token_id=tokenizer.eos_token_id      # 終了トークン指定
        )
    
    # 生成結果をテキストに変換
    generated_text = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True  # 特殊トークン（eos/pad）を除去
    )
    print(generated_text)