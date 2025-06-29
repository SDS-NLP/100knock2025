from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# モデルとトークナイザーの準備
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

prompt = "The movie was full of"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# 生成関数
def generate(method, temp=1.0, top_k=0, top_p=1.0):
    is_greedy = (method == 'greedy')
    outputs = model.generate(
        input_ids,
        max_length=20,
        do_sample=not is_greedy,
        temperature=temp,
        top_k=top_k,
        top_p=top_p,
        num_return_sequences=1 if is_greedy else 3,
        pad_token_id=tokenizer.eos_token_id
    )
    print(f"\n--- {method.upper()} (temperature={temp}) ---")
    for i, out in enumerate(outputs):
        print(f"{i+1}: {tokenizer.decode(out, skip_special_tokens=True)}")

# 各デコード方法で生成
generate("greedy")
generate("sampling", temp=1.0)
generate("sampling", temp=0.7)
generate("sampling", temp=1.5)
generate("top-k", temp=1.0, top_k=40)
generate("top-p", temp=1.0, top_p=0.9)
