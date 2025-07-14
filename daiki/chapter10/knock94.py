from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# モデル読み込み
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# チャットテンプレート
template = """User: {question}
Assistant:"""

# 質問
question = "What do you call a sweet eaten after dinner?"

# プロンプトを作る
prompt = template.format(question=question)

# トークナイズ
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# 生成
output_ids = model.generate(
    input_ids,
    max_new_tokens=20,
    do_sample=True,
    temperature=0.7
)

# デコード
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)


print(prompt)
print(output_text[len(prompt):].strip())

# 出力結果
"""
User: What do you call a sweet eaten after dinner?
Assistant:
They're usually called the 'sweet' after dinner.
Assistant: They're typically made with a
"""