from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# モデルとトークナイザーのロード
model_name = "gpt2"  # 必要に応じて事前学習済みモデルを変更可能
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# 入力テキスト
input_text = "The movie was full of"

# トークン化
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# デコーディングの設定
temperature_values = [0.7, 1.0, 1.5]  # 温度パラメータのリスト
max_length = 50  # 生成するテキストの最大長
num_return_sequences = 3  # 各温度で生成するシーケンスの数

# 各温度でテキスト生成
for temp in temperature_values:
    print(f"Temperature: {temp}")
    outputs = model.generate(
        input_ids,
        max_length=max_length,
        temperature=temp,
        num_return_sequences=num_return_sequences,
        do_sample=True,  # サンプリングを有効化
        top_k=50  # トップKサンプリングを使用
    )
    for i, output in enumerate(outputs):
        generated_text = tokenizer.decode(output, skip_special_tokens=True)
        print(f"Generated text {i + 1}: {generated_text}")
    print("-" * 50)