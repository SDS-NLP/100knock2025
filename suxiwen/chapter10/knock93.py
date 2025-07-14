from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# 1. モデルとトークナイザーの準備（GPT-2を使用）
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# GPT-2にはデフォルトでpad_tokenがないため、eos_tokenを代用
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()  # 評価モードに設定


def calculate_perplexity(sentence):
    """
    与えられた文のパープレキシティを計算する関数
    パープレキシティ = exp(-1 * 平均対数尤度)
    """
    # 文をトークン化（return_tensors="pt"でPyTorchテンソルに変換）
    inputs = tokenizer(
        sentence,
        return_tensors="pt",
        padding=True,  # パディングを有効化
        truncation=True  # 長い文は切り捨て
    )
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]  # パディング部分をマスク
    
    with torch.no_grad():  # 勾配計算を無効化
        # モデル出力を取得（labelsにinput_idsを指定すると自動で損失を計算）
        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=input_ids  # ラベルを入力と同じに設定（自己回帰的学習）
        )
    
    loss = outputs.loss  # クロスエントロピー損失（平均対数尤度の負の値）
    perplexity = torch.exp(loss).item()  # パープレキシティを計算（exp(loss)）
    return perplexity


# 2. 評価対象の4つの文（文法的に正しい文と誤った文を含む）
sentences = [
    "The movie was full of surprises",  # 正しい（単数主語 + was）
    "The movies were full of surprises", # 正しい（複数主語 + were）
    "The movie were full of surprises",  # 誤り（単数主語 + were）
    "The movies was full of surprises"   # 誤り（複数主語 + was）
]

# 3. 各文のパープレキシティを計算して表示
print("=== 各文のパープレキシティ測定結果 ===")
for i, sent in enumerate(sentences, 1):
    ppl = calculate_perplexity(sent)
    print(f"文{i}: {sent}")
    print(f"   パープレキシティ: {ppl:.2f}\n")