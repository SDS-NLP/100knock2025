from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import torch.nn.functional as F

# モデルとトークナイザをロード
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# 入力プロンプト
prompt = "The movie was full of"
input_ids = tokenizer.encode(prompt, return_tensors="pt")
attention_mask = torch.ones_like(input_ids)

# max_new_tokens: 生成する新規トークン数（短めに）
max_new_tokens = 10

# モデルによる生成
with torch.no_grad():
    output_ids = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=1.0,
        return_dict_in_generate=True,
        output_scores=True,
    )

# 出力トークン列（プロンプト＋生成）
all_tokens = output_ids.sequences[0]
scores = output_ids.scores

# トークンと確率を表示（プロンプト以降だけ）
print(f"\n[Prompt] {prompt}")
print("\n[Generated tokens and probabilities]\n")

for i, logits in enumerate(scores):
    token_id = all_tokens[len(input_ids[0]) + i].item()
    token_str = tokenizer.decode([token_id])

    probs = F.softmax(logits, dim=-1)
    prob = probs[0, token_id].item()

    print(f"{i+1:02d}: '{token_str}'  (token_id: {token_id},  prob: {prob:.6f})")
