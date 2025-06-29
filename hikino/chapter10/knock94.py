from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# モデルとトークナイザーの読み込み
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

# プロンプトの準備
prompt = "Q: What do you call a sweet eaten after dinner?\nA:"

# トークン化
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# テキスト生成
output_ids = model.generate(
    input_ids,
    max_new_tokens=20,
    do_sample=False,            # Greedy decoding
    pad_token_id=tokenizer.eos_token_id
)

# 結果のデコードと表示
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(output_text)
