# https://spacy.io/usage でのspacyのインストール
# pip install ja-ginza

from melos import text
import spacy

# 係り受け解析
nlp = spacy.load("ja_ginza")
doc = nlp(text)

# 係り受け関係の抽出
for token in doc:
    if token.dep_ != "ROOT":
        source = token.text
        target = token.head.text
        print(f"{source}\t{target}")