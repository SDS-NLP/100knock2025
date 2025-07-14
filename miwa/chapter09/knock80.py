#80. トークン化
from transformers import BertTokenizer

# BERTの英語トークナイザー
# uncasedは大文字小文字を区別しない
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# 対象文
sentence = "The movie was full of incomprehensibilities."

# トークン分割（文字列のまま表示）
tokens = tokenizer.tokenize(sentence)

print("トークン列:")
print(tokens)
