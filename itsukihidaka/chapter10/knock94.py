from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# モデルとトークナイザーの準備
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# チャットテンプレートの作成
question = "What do you call a sweet eaten after dinner?"
chat_prompt = f"Human: {question}\nAI:"

# トークナイズ
input_ids = tokenizer.encode(chat_prompt, return_tensors="pt")

# 応答生成
with torch.no_grad():
    output_ids = model.generate(
        input_ids,
        max_length=50,  # 全体長（入力含む）
        do_sample=True,
        temperature=0.9,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id
    )

# 出力から応答部分を抽出・表示
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# 応答部分の切り出し（"AI:" 以降）
response = output_text.split("AI:")[-1].strip()

print(f"\n[Prompt]")
print(chat_prompt)
print(f"\n[Model Response]")
print(response)
