# knock81.py
# BERTを使って[MASK]トークンに入る単語を予測するスクリプト

from transformers import BertTokenizer, BertForMaskedLM
import torch

def main():
    # 1. トークナイザーとモデルを読み込む
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertForMaskedLM.from_pretrained("bert-base-uncased")
    model.eval()  # 評価モード（推論モード）

    # 2. 入力文（[MASK]入り）
    sentence = "The movie was full of [MASK]."

    # 3. トークン化（エンコード）してテンソル化
    inputs = tokenizer(sentence, return_tensors="pt")

    # 4. モデルに入力して予測を取得
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    # 5. [MASK]トークンの位置を取得
    mask_token_index = (inputs["input_ids"] == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]

    # 6. [MASK]位置の予測スコアから上位5件を取得
    mask_logits = logits[0, mask_token_index, :]
    top_k = 5
    top_tokens = torch.topk(mask_logits, top_k, dim=1).indices[0].tolist()

    print(f"📘 入力文：{sentence}")
    print("🤖 [MASK] に入る候補トークン（上位5件）：")
    for token_id in top_tokens:
        token = tokenizer.decode([token_id])
        print(f"  - {token}")

if __name__ == "__main__":
    main()
