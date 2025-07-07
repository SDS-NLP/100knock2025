# knock84.py
# BERTの最終層のトークンベクトルの平均を用いて文のコサイン類似度を計算するスクリプト

from transformers import BertTokenizer, BertModel
import torch
import torch.nn.functional as F
import itertools

def get_average_embedding(sentence, tokenizer, model):
    """文から全トークンのベクトル平均を取得する関数"""
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    # 全トークンのベクトルを平均（次元: [トークン数, 隠れ層次元] → [隠れ層次元]）
    token_embeddings = outputs.last_hidden_state[0]  # shape: [seq_len, hidden_size]
    avg_embedding = token_embeddings.mean(dim=0)
    return avg_embedding

def main():
    # トークナイザーとモデルの読み込み
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertModel.from_pretrained("bert-base-uncased")
    model.eval()

    # 対象文
    sentences = [
        "The movie was full of fun.",
        "The movie was full of excitement.",
        "The movie was full of crap.",
        "The movie was full of rubbish."
    ]

    # 文ごとの平均ベクトルを取得
    embeddings = {sent: get_average_embedding(sent, tokenizer, model) for sent in sentences}

    # 組み合わせごとにコサイン類似度を計算
    print("📊 文ペア間のコサイン類似度（平均ベクトル）：")
    for sent1, sent2 in itertools.combinations(sentences, 2):
        vec1 = embeddings[sent1]
        vec2 = embeddings[sent2]
        similarity = F.cosine_similarity(vec1, vec2, dim=0).item()
        print(f"- 「{sent1}」 vs 「{sent2}」: 類似度 = {similarity:.4f}")

if __name__ == "__main__":
    main()
