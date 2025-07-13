from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
sentence = "The movie was full of incomprehensibilities."
tokens = tokenizer.tokenize(sentence)

print(tokens)