from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 事前学習済みのGPT-2モデルとトークナイザーをロード
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# チャットのテンプレートとプロンプトを定義
question = "What do you call a sweet eaten after dinner?"
chat_template = "Q: {}\nA:".format(question)

# 入力プロンプトをトークン化
inputs = tokenizer.encode(chat_template, return_tensors="pt")

# 応答を生成
outputs = model.generate(inputs, max_length=50, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# 応答を表示
print(response)