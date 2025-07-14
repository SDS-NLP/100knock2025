from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# モデルとトークナイザのロード
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# チャットテンプレートに基づくプロンプト
prompt = "<|user|>\nWhat do you call a sweet eaten after dinner?\n<|assistant|>\n"

# トークン化
input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

# 応答生成
output = model.generate(
    input_ids,
    max_new_tokens=20,
    do_sample=True,
    temperature=0.9,
    top_p=0.95,
    pad_token_id=tokenizer.eos_token_id
)

# 結果表示
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
# 応答部分だけ抽出
response = generated_text.split("<|assistant|>")[-1].strip()
print(f"Model's answer: {response}")
