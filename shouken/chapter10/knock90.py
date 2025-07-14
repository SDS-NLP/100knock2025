from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import torch.nn.functional as F

# モデルとトークナイザーの準備（GPT2を使用）
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# GPUが利用可能ならGPUへ
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 入力文
input_text = "The movie was full of"

# トークン列に変換し、テンソル化（batch次元を追加）
input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)

# トークン列の確認（可読化）
tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
print("入力トークン列:", tokens)

# モデルに入力してロジットを取得
with torch.no_grad():
    outputs = model(input_ids)
    logits = outputs.logits  # [batch, seq_len, vocab_size]

# 最後のトークン位置のロジットを抽出
last_token_logits = logits[0, -1, :]

# softmaxで確率化
probs = F.softmax(last_token_logits, dim=-1)

# 上位10個のトークンとその確率を取得
top_k = 10
top_probs, top_indices = torch.topk(probs, top_k)

# トークンと確率を表示
print("\n【次トークン予測：上位10個】")
for i in range(top_k):
    token_str = tokenizer.decode([top_indices[i]])
    prob = top_probs[i].item()
    print(f"{i+1:>2}: '{token_str}'\t確率: {prob:.4f}")

'''
【出力結果】
入力トークン列: ['The', 'Ġmovie', 'Ġwas', 'Ġfull', 'Ġof']

【次トークン予測：上位10個】
 1: ' jokes'    確率: 0.0219
 2: ' great'    確率: 0.0186
 3: ' laughs'   確率: 0.0115
 4: ' bad'      確率: 0.0109
 5: ' surprises'        確率: 0.0107
 6: ' references'       確率: 0.0105
 7: ' fun'      確率: 0.0100
 8: ' humor'    確率: 0.0074
 9: ' "'        確率: 0.0074
10: ' the'      確率: 0.0067
'''