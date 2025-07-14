"""
knock80:トークン化
“The movie was full of incomprehensibilities.”という文を
トークンに分解し、トークン列を表示せよ。
"""
from transformers import BertTokenizer

#BERTベースモデルのトークナイザを読み込む
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

#対象文
sentence = "The movie was full of incomprehensibilities."

#トークン化（WordPiece）
tokens = tokenizer.tokenize(sentence)

#結果表示
print(tokens)
