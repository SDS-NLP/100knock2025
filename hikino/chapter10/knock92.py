from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import torch.nn.functional as F

# モデルとトークナイザーの準備
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

prompt = "The movie was full of"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# 生成：最大10トークン（+入力分）までに制限
max_new_tokens = 10
output_ids = model.generate(
    input_ids,
    max_new_tokens=max_new_tokens,
    do_sample=False,  # greedy decoding
    return_dict_in_generate=True,
    output_scores=True  # スコアを取る
)

# 出力トークンと対応するスコアを表示
generated_ids = output_ids.sequences[0]
scores = output_ids.scores  # 各ステップでの vocab_size 分のlogits

# 入力部分を除いた生成トークンに対応するスコアだけ扱う
new_token_ids = generated_ids[len(input_ids[0]):]

print(f"\nPrompt: {prompt}")
print("Generated text:", tokenizer.decode(new_token_ids, skip_special_tokens=True))
print("\nGenerated tokens and their probabilities:")

for i, (token_id, score_logits) in enumerate(zip(new_token_ids, scores)):
    prob = F.softmax(score_logits.squeeze(), dim=-1)[token_id].item()
    token_str = tokenizer.decode([token_id])
    print(f"{i+1:2d}. {token_str:<12} (probability: {prob:.5f})")
