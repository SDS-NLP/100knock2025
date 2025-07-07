# knock80.py
# BERTのトークナイザーで英文をトークン化するスクリプト
# 80. トークン化
# “The movie was full of incomprehensibilities.”という文をトークンに分解し、トークン列を表示せよ。

from transformers import BertTokenizer

def main():
    # 使用する事前学習済みモデルに対応したトークナイザーをロード
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    # トークン化したい文
    sentence = "The movie was full of incomprehensibilities."

    # トークン化（サブワード単位で分割）
    tokens = tokenizer.tokenize(sentence)

    # 結果表示
    print("📘 入力文：", sentence)
    print("🧩 トークン列：", tokens)

if __name__ == "__main__":
    main()
