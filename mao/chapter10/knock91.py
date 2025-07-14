"""
knock91:続きのテキストの予測
“The movie was full of”に続くテキストを複数予測せよ。
このとき、デコーディングの方法や温度パラメータ（temperature）を変えながら、
予測される複数のテキストの変化を観察せよ。
"""
#GPUじゃないと動かなさそう
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

prompt = "The movie was full of"
input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
attention_mask = torch.ones_like(input_ids)  # 明示的なマスク

output = model.generate(
    input_ids,
    attention_mask=attention_mask,
    max_length=30,
    temperature=1.0,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id  # これも必要
)

print(tokenizer.decode(output[0], skip_special_tokens=True))
