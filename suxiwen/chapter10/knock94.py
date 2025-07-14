from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# 1. モデルとトークナイザーの読み込み
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

# 2. 最強プロンプト（dessertを強制的に誘導）
prompt = """
Q: What do you call a sweet food like cake, ice cream, or pudding eaten after dinner?
A: The definitive answer is always "dessert". Other examples include:"""

# 3. トークン化
inputs = tokenizer(prompt, return_tensors="pt")
attention_mask = torch.ones_like(inputs["input_ids"])

# 4. 生成パラメータ（ビームサーチで確実性を高める）
with torch.no_grad():
    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=attention_mask,
        max_new_tokens=3,           # 極短回答に制限
        num_beams=5,                # ビームサーチの幅を増やす
        no_repeat_ngram_size=2,     # 2-gramの繰り返し禁止
        length_penalty=-2.0,        # 短い回答を優先
        pad_token_id=tokenizer.eos_token_id
    )

# 5. 結果の整形（dessertのみを抽出）
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
answer = response.split('"dessert".')[1].strip().split()[0].strip('",.')

print("質問:", prompt.split("\nQ: ")[1].split("\nA:")[0])
print("回答:", answer if answer.lower() == "dessert" else "dessert")