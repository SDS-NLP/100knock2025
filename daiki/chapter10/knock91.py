from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# モデルとトークナイザ準備
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# 入力プロンプト
prompt = "The movie was full of"

# トークン化
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# temperature の値を変えて試す
temperatures = [0.3, 1.0, 2.0]

# デコーディング手法例
# do_sample=True → サンプリング
# top_k → k個まで絞る（上位k単語）
# top_p → nucleus sampling (確率の累積でpまで残す)
# max_new_tokens → 生成するトークン数
for temp in temperatures:
    print(f"\n Temperature = {temp} ")
    
    output_ids = model.generate(
        input_ids,
        max_new_tokens=30, # 新しく生成する最大トークン数
        temperature=temp,
        do_sample=True, # 確率に従ってランダムに単語を選ぶ
        top_k=50,      # トップ50から選ぶ
        top_p=0.9,     # 累確率を合計して 0.9 を超えない範囲の単語だけ残す
        num_return_sequences=3,   # 3パターンのテキストを生成
    )
    
    for i, seq in enumerate(output_ids):
        text = tokenizer.decode(seq, skip_special_tokens=True)
        print(f"[{i+1}] {text}")
