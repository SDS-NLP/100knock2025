from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# 1. GPT-2モデルとトークナイザーの読み込み
# GPT-2はTransformerデコーダ型モデルで、次単語予測を基本タスクとする
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# GPT-2にはデフォルトでpad_tokenが設定されていないため、eos_tokenを代用
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()  # 評価モードに設定（学習時のドロップアウトなどを無効化）

# 2. 入力プロンプトの準備
prompt = "The movie was full of"
# プロンプトをトークン化（テキスト -> トークンIDのテンソルに変換）
inputs = tokenizer(prompt, return_tensors="pt")  # return_tensors="pt"でPyTorchテンソル形式に
input_ids = inputs["input_ids"]  # トークンIDの配列（形状: [1, シーケンス長]）

# 3. 生成設定（適切な長さで打ち切るため、新しく生成するトークン数を10に制限）
max_new_tokens = 10  # 生成する最大トークン数（過剰に長くならないよう調整）
generated_ids = input_ids.clone()  # 生成過程のトークンIDを保存する変数（初期値は入力のトークン列）

# 生成されたトークンとその尤度を保存するリスト
generated_tokens = []  # 生成されたトークン（文字列）を格納
token_likelihoods = []  # 各トークンの尤度（条件付き確率）を格納

# 4. 逐次的にテキストを生成し、各トークンの尤度を計算
# 尤度とは、「前文が与えられたときに当該トークンが出現する確率」を意味する
with torch.no_grad():  # 勾配計算を無効化（推論時に不要）
    for _ in range(max_new_tokens):
        # 現在のトークン列を入力し、モデルからlogitsを取得
        outputs = model(generated_ids)
        logits = outputs.logits  # logits: 各位置の未正規化確率（形状: [1, 現在の長さ, 語彙数]）
        
        # 最後の位置のlogitsを抽出（次のトークンの予測分布）
        next_token_logits = logits[:, -1, :]  # 形状: [1, 語彙数]
        
        # logitsをsoftmaxで正規化し、確率分布に変換
        next_token_probs = torch.softmax(next_token_logits, dim=-1).squeeze()  # 形状: [語彙数]
        
        # 貪欲探索で最も確率の高いトークンを選択
        next_token_id = torch.argmax(next_token_probs).item()  # 最も高い確率のトークンID
        next_token_prob = next_token_probs[next_token_id].item()  # そのトークンの確率（尤度）
        
        # トークンIDを文字列に変換し、リストに保存
        generated_token = tokenizer.convert_ids_to_tokens(next_token_id)
        generated_tokens.append(generated_token)
        token_likelihoods.append(next_token_prob)
        
        # 生成したトークンIDをシーケンスに追加し、次のステップへ
        next_token_tensor = torch.tensor([[next_token_id]], dtype=torch.long)
        generated_ids = torch.cat([generated_ids, next_token_tensor], dim=-1)

# 5. 生成された全文を復元
generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

# 6. 結果の表示
print("=== 生成された全文 ===")
print(generated_text)
print("\n=== 各トークンの尤度（条件付き確率） ===")
print(f"入力プロンプトのトークン: {tokenizer.convert_ids_to_tokens(input_ids[0])}")
for i in range(len(generated_tokens)):
    # GPT-2のトークンに含まれる特殊記号「Ġ」をスペースに置換して表示
    clean_token = generated_tokens[i].replace('Ġ', ' ')
    # 確率をパーセントで表示（小数点第2位まで）
    print(f"生成トークン {i+1}: {clean_token:10} | 尤度: {token_likelihoods[i]*100:.2f}%")

# 7. 生成系列全体の対数尤度（数値安定性のため）
log_likelihoods = [torch.log(torch.tensor(p)).item() for p in token_likelihoods]
total_log_likelihood = sum(log_likelihoods)
# 対数尤度を元の確率に変換（指数関数）
total_likelihood = torch.exp(torch.tensor(total_log_likelihood)).item()

print("\n=== 生成系列全体の確率 ===")
print(f"対数尤度の合計: {total_log_likelihood:.4f}")
print(f"全体の尤度（各トークンの条件付き確率の積）: {total_likelihood:.10f} ({total_likelihood*100:.8f}%)")