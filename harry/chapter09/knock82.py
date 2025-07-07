# knock82.py
# BERTを使って[MASK]のTop-10予測トークンとその確率を表示するスクリプト

from transformers import BertTokenizer, BertForMaskedLM
import torch
import torch.nn.functional as F

def main():
    # トークナイザーとモデルの準備
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertForMaskedLM.from_pretrained("bert-base-uncased")
    model.eval()

    # 入力文
    sentence = "The movie was full of [MASK]."
    inputs = tokenizer(sentence, return_tensors="pt")

    # モデル出力
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    # [MASK]トークンの位置
    mask_token_index = (inputs["input_ids"] == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]

    # [MASK]位置のlogits（生スコア）を取得しsoftmaxで確率に変換
    mask_logits = logits[0, mask_token_index, :].squeeze()
    probs = F.softmax(mask_logits, dim=-1)

    # 上位10件のトークンと確率
    top_k = 10
    top_probs, top_indices = torch.topk(probs, top_k)

    print(f"📘 入力文：{sentence}")
    print("🤖 [MASK] に入る候補トークン（上位10件）とその確率：")
    for prob, token_id in zip(top_probs.tolist(), top_indices.tolist()):
        token = tokenizer.decode([token_id])
        print(f"  - {token:<12} : {prob:.4f}")

if __name__ == "__main__":
    main()
