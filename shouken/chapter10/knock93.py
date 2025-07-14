from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import math

# モデルとトークナイザーの読み込み
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval().cuda()

# 評価対象の4文（2つは文法ミスあり）
sentences = [
    "The movie was full of surprises",    # 正常
    "The movies were full of surprises",  # 正常
    "The movie were full of surprises",   # 文法誤り
    "The movies was full of surprises",   # 文法誤り
]

# パープレキシティを計算する関数
def calculate_perplexity(sentence):
    input_ids = tokenizer.encode(sentence, return_tensors='pt').cuda()
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        loss = outputs.loss
    return math.exp(loss.item())

# 各文に対してPPLを測定して表示
print("=== 文ごとのパープレキシティ ===")
for sentence in sentences:
    ppl = calculate_perplexity(sentence)
    print(f"{sentence:<45} -> PPL = {ppl:.2f}")
