#92. 予測されたテキストの確率を計算
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import torch.nn.functional as F

# モデルとトークナイザーを読み込み
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# プロンプト
prompt = "The movie was full of"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# 最大生成トークン数（例：10）
max_new_tokens = 10

# 入力文の長さ
initial_length = input_ids.shape[1]

# テキスト生成（sampling）
output_ids = model.generate(
    input_ids=input_ids,
    max_new_tokens=max_new_tokens,
    do_sample=True,
    temperature=1.0,
    pad_token_id=tokenizer.eos_token_id,
    return_dict_in_generate=True,
    output_scores=True
)

# トークンID列（入力＋出力）
generated_ids = output_ids.sequences[0]
tokens = tokenizer.convert_ids_to_tokens(generated_ids)

# 各ステップのスコア（logitsからsoftmaxして尤度を得る）
scores = output_ids.scores  # 各stepのlogits（len = max_new_tokens）

print("生成されたトークンとその尤度（確率）:\n")

# 出力部分だけ取り出して表示
for i, score_tensor in enumerate(scores):
    probs = F.softmax(score_tensor, dim=-1)
    token_id = generated_ids[initial_length + i].item()
    token = tokenizer.convert_ids_to_tokens(token_id)
    prob = probs[0, token_id].item()
    print(f"[{i+1}] '{token}'\t尤度: {prob:.5f}")
