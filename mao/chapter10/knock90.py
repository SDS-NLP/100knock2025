"""
knock90:次単語予測
“The movie was full of”に続くトークン
（トークン列ではなく一つのトークンであることに注意せよ）として
適切なもの上位10個と、その確率（尤度）を求めよ。
ただし、言語モデルへのプロンプトがどのようなトークン列に変換されたか確認せよ。
"""
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# モデルとトークナイザの読み込み（GPT-2）
tokenizer = GPT2Tokenizer.from_pretrained("gpt2") #トークナイザー
model = GPT2LMHeadModel.from_pretrained("gpt2")   #モデル
model.eval()

# 入力文
prompt = "The movie was full of"

# トークナイズしてテンソル化、モデルへ入力可能な形へ
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# トークン列の確認
tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
print("プロンプトのトークン列:", tokens)

# モデルで予測
with torch.no_grad():
    outputs = model(input_ids)
    logits = outputs.logits

# 最後のトークンに対応するロジットから確率分布を計算
next_token_logits = logits[0, -1, :]
probs = torch.softmax(next_token_logits, dim=-1)

# 上位10個のトークンと確率を取得
top_k = 10
top_k_probs, top_k_indices = torch.topk(probs, top_k)
top_k_tokens = tokenizer.convert_ids_to_tokens(top_k_indices)

# 結果の表示
print("\n次の1トークンとして尤もらしい上位10語:")
for i in range(top_k):
    token = top_k_tokens[i]
    prob = top_k_probs[i].item()
    # スペース付きトークンの表示整形
    token_clean = token.replace("Ġ", " ")
    print(f"{i+1}. '{token_clean.strip()}': 確率 = {prob:.4f}")

"""
プロンプトのトークン列: ['The', 'Ġmovie', 'Ġwas', 'Ġfull', 'Ġof']
次の1トークンとして尤もらしい上位10語:
1. 'jokes': 確率 = 0.0219
2. 'great': 確率 = 0.0186
3. 'laughs': 確率 = 0.0115
4. 'bad': 確率 = 0.0109
5. 'surprises': 確率 = 0.0107
6. 'references': 確率 = 0.0105
7. 'fun': 確率 = 0.0100
8. 'humor': 確率 = 0.0074
9. '"': 確率 = 0.0074
10. 'the': 確率 = 0.0067
"""