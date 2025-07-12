# knock91.py
# 目的: GPT2で「The movie was full of」の続きを、異なる生成条件で複数生成

from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# モデルとトークナイザーを読み込み
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# 入力プロンプトとトークン化
prompt = "The movie was full of"
inputs = tokenizer(prompt, return_tensors="pt")
input_ids = inputs.input_ids
attention_mask = inputs.attention_mask

# 生成の設定（greedyとsamplingを比較）
configs = [
    {"name": "greedy", "do_sample": False, "temperature": 1.0},
    {"name": "sampling_T0.7", "do_sample": True, "temperature": 0.7},
    {"name": "sampling_T1.0", "do_sample": True, "temperature": 1.0},
]

# 各設定で生成
for config in configs:
    print(f"\n=== 🔧 デコード方法: {config['name']} ===")
    for i in range(3):  # 同じ条件で3回生成
        # 共通引数
        generate_kwargs = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "max_length": 30,
            "do_sample": config["do_sample"],
            "temperature": config["temperature"],
            "pad_token_id": tokenizer.eos_token_id
        }

        # sampling の場合のみ top_k, top_p を設定
        if config["do_sample"]:
            generate_kwargs["top_k"] = 50
            generate_kwargs["top_p"] = 0.95

        # 生成
        output_ids = model.generate(**generate_kwargs)
        generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        print(f"{i+1} ➡️ {generated_text}")
