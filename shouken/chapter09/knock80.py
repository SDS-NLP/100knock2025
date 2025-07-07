from transformers import BertTokenizer

# トークナイザの読み込み（英語、uncased）
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# 入力文
text = "The movie was full of incomprehensibilities."

# トークン化
tokens = tokenizer.tokenize(text)

# 表示
print(tokens)
