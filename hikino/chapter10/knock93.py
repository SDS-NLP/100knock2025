from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import math

# モデルとトークナイザー
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

# パープレキシティ計算関数
def calculate_perplexity(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")
    input_ids = inputs["input_ids"]
    
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        # CrossEntropyLoss を内部で計算してくれる（mean over tokens）
        loss = outputs.loss
    return math.exp(loss.item())

# 文とPPLの表示
sentences = [
    "The movie was full of surprises",
    "The movies were full of surprises",
    "The movie were full of surprises",
    "The movies was full of surprises"
]

print("Sentence                          | Perplexity")
print("----------------------------------|-----------")
for sent in sentences:
    ppl = calculate_perplexity(sent)
    print(f"{sent:<34} | {ppl:.2f}")
