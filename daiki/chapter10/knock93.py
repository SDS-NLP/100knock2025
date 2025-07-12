from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import torch.nn.functional as F
import math

# モデルとトークナイザの準備
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# 文のリスト
sentences = [
    "The movie was full of surprises",
    "The movies were full of surprises",
    "The movie were full of surprises",
    "The movies was full of surprises"
]

print("Perplexity Calculation\n")

for sentence in sentences:
    # テキストをトークン化
    encodings = tokenizer(sentence, return_tensors="pt") # テキストをトークンIDに変換 # return_tensors="pt" で PyTorch の tensor で返す
    input_ids = encodings.input_ids # トークンID部分だけ取り出す

    # モデル出力
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        # 負の対数尤度の平均 loss が自動で計算される
        # モデルが「この文章どれだけ予測しやすかったか」を出してくれる
        loss = outputs.loss

    # perplexity 計算
    ppl = math.exp(loss.item())

    print(f"Sentence: {sentence}")
    print(f"Perplexity: {ppl:.2f}\n")

# 出力結果
"""
Perplexity Calculation

Sentence: The movie was full of surprises
Perplexity: 99.35

Sentence: The movies were full of surprises
Perplexity: 126.48

Sentence: The movie were full of surprises
Perplexity: 278.88

Sentence: The movies was full of surprises
Perplexity: 274.66
"""