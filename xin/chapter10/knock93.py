import torch
import torch.nn.functional as F
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import math

# モデルとトークナイザのロード
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# パープレキシティ計算関数
def calculate_perplexity(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)

    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        loss = outputs.loss  # クロスエントロピー損失

    ppl = torch.exp(loss).item()
    return ppl

# テスト文
sentences = [
    "The movie was full of surprises",
    "The movies were full of surprises",
    "The movie were full of surprises",
    "The movies was full of surprises"

]

# 結果表示
for s in sentences:
    ppl = calculate_perplexity(s)
    print(f"Sentence: {s}\n→ Perplexity: {ppl:.4f}\n")
