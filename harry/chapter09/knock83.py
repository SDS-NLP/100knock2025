# knock83.py
# BERTの[CLS]トークンを用いて文のコサイン類似度を計算するスクリプト

from transformers import BertTokenizer, BertModel
import torch
import torch.nn.functional as F
import itertools

def get_cls_embedding(sentence, tokenizer, model):
    """文をトークン化し、[CLS]トークンのベクトルを取得する関数"""
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    # 最終層の[CLS]トークンのベクトル（位置0）
    cls_embedding = outputs.last_hidden_state[0, 0, :]
    return cls_embedding

def main():
    # モデルとトークナイザーの準備
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertModel.from_pretrained("bert-base-uncased")
    model.eval()

    # 対象の文
    sentences = [
        "The movie was full of fun.",
        "The movie was full of excitement.",
        "The movie was full of crap.",
        "The movie was full of rubbish."
    ]

    # 各文の[CLS]ベクトルを取得
    embeddings = {sent: get_cls_embedding(sent, tokenizer, model) for sent in sentences}

    # 全ての組み合わせに対してコサイン類似度を計算
    print("📊 文ペア間のコサイン類似度：")
    for sent1, sent2 in itertools.combinations(sentences, 2):
        vec1 = embeddings[sent1]
        vec2 = embeddings[sent2]
        similarity = F.cosine_similarity(vec1, vec2, dim=0).item()
        print(f"- 「{sent1}」 vs 「{sent2}」: 類似度 = {similarity:.4f}")

if __name__ == "__main__":
    main()
