from transformers import GPT2Tokenizer, GPT2LMHeadModel 
# GPT2Tokenizer は文字列トークンに分割し、数値のIDに変換するツール
# GPT2LMHeadModel は次に来る単語を予測するタスクができるGPT-2 の言語モデル本体
import torch
import torch.nn.functional as F

# モデルとトークナイザの準備
model_name = "gpt2"  # 小さめのGPT-2
tokenizer = GPT2Tokenizer.from_pretrained(model_name) # 事前学習済みのトークナイザをダウンロードして読み込む
model = GPT2LMHeadModel.from_pretrained(model_name) # 事前学習済みの GPT-2 モデル をダウンロードして読み込む
model.eval() # 推論モード に切り替える

# 入力文
text = "The movie was full of"

# トークナイズ（ID化）
input_ids = tokenizer.encode(text, return_tensors="pt") # 文字列 → トークンIDの列に変換する関数

# モデル出力取得
with torch.no_grad():
    outputs = model(input_ids)
    # 出力の last token の logits を取り出す
    next_token_logits = outputs.logits[0, -1, :] # 「次に続く単語がそれぞれどれくらい出そうか」モデルの生スコア

# ソフトマックスで確率化 logits → 確率 に変換
probs = F.softmax(next_token_logits, dim=-1)

# 上位10個の単語IDと確率を取得
top_k = 10
top_probs, top_indices = torch.topk(probs, top_k)

# 結果表示
for i in range(top_k):
    token_id = top_indices[i].item()
    token_str = tokenizer.decode([token_id])
    prob = top_probs[i].item()
    print(f"Token: {repr(token_str)}\tProbability: {prob:.5f}")

# 入力がどのトークン列に変換されたか表示
tokens = tokenizer.convert_ids_to_tokens(input_ids[0]) # トークンID → トークン文字列 に変換する関数
print("\nPrompt tokens:", tokens)

# 出力結果
"""
Token: ' jokes' Probability: 0.02189
Token: ' great' Probability: 0.01864
Token: ' laughs'        Probability: 0.01152
Token: ' bad'   Probability: 0.01087
Token: ' surprises'     Probability: 0.01067
Token: ' references'    Probability: 0.01053
Token: ' fun'   Probability: 0.00999
Token: ' humor' Probability: 0.00742
Token: ' "'     Probability: 0.00741
Token: ' the'   Probability: 0.00671

Prompt tokens: ['The', 'Ġmovie', 'Ġwas', 'Ġfull', 'Ġof']
"""
# Ġ は空白を表す記号