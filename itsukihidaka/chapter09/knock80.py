# “The movie was full of incomprehensibilities.”という文をトークンに分解し、トークン列を表示せよ。

from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
sentence = "The movie was full of incomprehensibilities."
tokens = tokenizer.tokenize(sentence)
print(tokens)       # 表示
