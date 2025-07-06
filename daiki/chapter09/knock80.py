from transformers import BertTokenizer

# 事前学習済みの「bert-base-cased」というBERTのトークナイザを読み込み
tokenizer = BertTokenizer.from_pretrained("bert-base-cased")


# 入力文
text = "The movie was full of incomprehensibilities."

# トークン化
tokens = tokenizer.tokenize(text)

# 結果表示
print(tokens)

# 結果
# ['The', 'movie', 'was', 'full', 'of', 'inc', '##omp', '##re', '##hen', '##si', '##bilities', '.']
# BERTでは単語をサブワード単位で分割するため、incomprehensibilities が細かいサブワードに分かれている