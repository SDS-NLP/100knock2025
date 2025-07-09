from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# モデルとトークナイザーの準備
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 入力文
prompt = "The movie was full of"
input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)

# デコード設定をまとめる（比較用）
settings = [
    {"method": "greedy", "do_sample": False, "temperature": 1.0},
    {"method": "beam search", "num_beams": 5, "do_sample": False, "temperature": 1.0},
    {"method": "sampling (T=0.7)", "do_sample": True, "temperature": 0.7},
    {"method": "sampling (T=1.0)", "do_sample": True, "temperature": 1.0},
    {"method": "sampling (T=1.5)", "do_sample": True, "temperature": 1.5},
]

# 各設定でテキスト生成
for setting in settings:
    print(f"\n--- {setting['method']} ---")
    gen_kwargs = {
        "max_new_tokens": 30,
        "do_sample": setting.get("do_sample", False),
        "temperature": setting.get("temperature", 1.0),
    }
    # ビームサーチの場合
    if setting["method"] == "beam search":
        gen_kwargs["num_beams"] = setting["num_beams"]

    output = model.generate(input_ids, **gen_kwargs)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(generated_text)
