#94.チャットテンプレート
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# モデルとトークナイザー
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

# チャット風のプロンプト
prompt = """System: You are a helpful assistant.
User: What do you call a sweet eaten after dinner?
Assistant:"""

# トークン化
inputs = tokenizer(prompt, return_tensors="pt")
input_ids = inputs["input_ids"]
attention_mask = inputs["attention_mask"]

# 応答生成
output_ids = model.generate(
    input_ids,
    attention_mask=attention_mask,
    max_new_tokens=30,
    do_sample=True,
    temperature=0.9,
    pad_token_id=tokenizer.eos_token_id
)

# 出力のデコード
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Assistantの返答部分だけ抽出
assistant_reply = output_text.split("Assistant:")[-1].split("User:")[0].strip()
print("Assistantの応答:")
print(assistant_reply)
