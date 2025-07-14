from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# モデル・トークナイザのロード
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# 入力プロンプト
prompt = "The movie was full of"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# 各手法のパラメータ設定
decoding_configs = [
    {
        "name": "Greedy",
        "params": {
            "do_sample": False,
            "num_return_sequences": 1,
        }
    },
    {
        "name": "Beam Search (beam_width=5)",
        "params": {
            "do_sample": False,
            "num_beams": 5,
            "num_return_sequences": 5,
            "early_stopping": True,
        }
    },
    {
        "name": "Sampling (T=1.0)",
        "params": {
            "do_sample": True,
            "temperature": 1.0,
            "num_return_sequences": 3,
        }
    },
    {
        "name": "Top-k sampling (k=50)",
        "params": {
            "do_sample": True,
            "top_k": 50,
            "temperature": 1.0,
            "num_return_sequences": 3,
        }
    },
    {
        "name": "Top-p sampling (p=0.9)",
        "params": {
            "do_sample": True,
            "top_p": 0.9,
            "temperature": 1.0,
            "num_return_sequences": 3,
        }
    }
]

# 各方式で生成
max_length = 30  # 入力＋出力トークンの合計

for config in decoding_configs:
    print(f"\n--- {config['name']} ---")
    gen_outputs = model.generate(
        input_ids=input_ids,
        max_length=max_length,
        pad_token_id=tokenizer.eos_token_id,
        **config["params"]
    )
    
    for i, output in enumerate(gen_outputs):
        decoded = tokenizer.decode(output, skip_special_tokens=True)
        print(f"[{i+1}] {decoded}")
