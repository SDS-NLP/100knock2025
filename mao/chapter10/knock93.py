"""
knock93:パープレキシティ
適当な文を準備して、事前学習済み言語モデルでパープレキシティを測定せよ。
例えば、
The movie was full of surprises
The movies were full of surprises
The movie were full of surprises
The movies was full of surprises
の4文に対して、パープレキシティを測定して観察せよ
（最後の2つの文は故意に文法的な間違いを入れた）。
"""
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import torch.nn.functional as F
import math

# モデルとトークナイザの準備
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()
model.to("cpu")  # Macなら安全のためGPUは避ける

# パープレキシティ計算関数
def calculate_ppl(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask, labels=input_ids)
        # CrossEntropyLossの average loss（token単位）
        loss = outputs.loss
        ppl = torch.exp(loss)
    return ppl.item()

# 評価文（正しい/間違った英文）
sentences = [
    "The movie was full of surprises",      # ✅ 正しい
    "The movies were full of surprises",    # ✅ 正しい
    "The movie were full of surprises",     # ❌ 文法ミス
    "The movies was full of surprises"      # ❌ 文法ミス
]

# 実行して結果表示
print("📊 各文のパープレキシティ:")
for sentence in sentences:
    ppl = calculate_ppl(sentence)
    print(f"'{sentence}': PPL = {ppl:.2f}")
"""


"""

