# knock94.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 制限なしで使えるチャットモデル（軽量）
model_name = "tiiuae/falcon-rw-1b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.eval()

# プロンプト（直接1文で入力）
prompt = "What do you call a sweet eaten after dinner?"

# テキストをトークン化
inputs = tokenizer(prompt, return_tensors="pt")
input_ids = inputs["input_ids"]

# 応答生成
with torch.no_grad():
    outputs = model.generate(
        input_ids=input_ids,
        max_new_tokens=50,
        do_sample=True,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id
    )

# 出力をデコードして表示
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(f"📝 質問: {prompt}")
print(f"💬 応答: {generated_text[len(prompt):].strip()}")
