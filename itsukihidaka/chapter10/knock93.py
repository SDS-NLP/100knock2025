from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import torch.nn.functional as F
import math

# モデル・トークナイザのロード
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# 評価対象の文
sentences = [
    "The movie was full of surprises",
    "The movies were full of surprises",
    "The movie were full of surprises",   # 文法ミス
    "The movies was full of surprises"    # 文法ミス
]

def calculate_perplexity(sentence):
    # トークナイズして入力に変換
    inputs = tokenizer(sentence, return_tensors="pt")
    input_ids = inputs["input_ids"]

    # ラベルとして自分自身を使う（next-token prediction）
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        loss = outputs.loss  # クロスエントロピー（平均）

    # PPL = exp(loss)
    ppl = torch.exp(loss).item()
    return ppl

# 各文について PPL を計算
print("\n[Perplexity Results]\n")
for s in sentences:
    ppl = calculate_perplexity(s)
    print(f"'{s}'  →  Perplexity: {ppl:.2f}")
