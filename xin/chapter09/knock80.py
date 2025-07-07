from transformers import BertTokenizer

# トークナイザーの準備
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# 対象の文
sentence = "The movie was full of incomprehensibilities."

# トークン化
tokens = tokenizer.tokenize(sentence)

# トークン列を表示
print(tokens)