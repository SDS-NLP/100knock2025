#パープレキシティ
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import math

# モデルとトークナイザーの読み込み
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# 評価対象の文
sentences = [
    "The movie was full of surprises",      
    "The movies were full of surprises",    
    "The movie were full of surprises",     
    "The movies was full of surprises"      
]

# perplexity 計算関数
def calculate_perplexity(sentence):
    encodings = tokenizer(sentence, return_tensors="pt")
    input_ids = encodings.input_ids
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        loss = outputs.loss  # CrossEntropyLoss
    return math.exp(loss.item())

# 計算・表示
print("文ごとのパープレキシティ:\n")
for s in sentences:
    ppl = calculate_perplexity(s)
    print(f"\"{s}\" \n→ Perplexity: {ppl:.2f}\n")
