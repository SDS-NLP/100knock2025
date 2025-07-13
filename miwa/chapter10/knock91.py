#91. 続きのテキストの予測
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# モデルとトークナイザー
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

prompt = "The movie was full of"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# 各種設定で生成
def generate_and_print(strategy_name, **kwargs):
    print(f"Strategy: {strategy_name}")
    output_ids = model.generate(
        input_ids,
        max_new_tokens=30,
        do_sample=kwargs.get("do_sample", False),
        temperature=kwargs.get("temperature", 1.0),
        top_k=kwargs.get("top_k", 0),
        top_p=kwargs.get("top_p", 1.0),
        num_return_sequences=kwargs.get("num_return_sequences", 3),
        pad_token_id=tokenizer.eos_token_id
    )
    for i, output in enumerate(output_ids):
        text = tokenizer.decode(output, skip_special_tokens=True)
        print(f"  [{i+1}] {text}")

# ① Greedy decoding（決定論的）
generate_and_print("Greedy decoding", do_sample=False, num_return_sequences=1)

# ② Sampling（高温度）
generate_and_print("Sampling (temperature=1.5)", do_sample=True, temperature=1.5)

# ③ Top-k sampling（k=50, 温度=1.0）
generate_and_print("Top-k sampling (k=50)", do_sample=True, top_k=50, temperature=1.0)

# ④ Top-p (nucleus) sampling（p=0.9）
generate_and_print("Top-p sampling (p=0.9)", do_sample=True, top_p=0.9, temperature=1.0)
