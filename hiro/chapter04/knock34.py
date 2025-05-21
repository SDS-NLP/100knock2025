from melos import text
import spacy

# 係り受け解析
nlp = spacy.load("ja_ginza")
doc = nlp(text)

# 述語の抽出
predicates = []
for token in doc:
    if token.text == "メロス" and token.dep_ == "nsubj": # 名詞的主語であるメロスの判定
        predicate = token.head
        predicates.append(predicate.text)


print(predicates)