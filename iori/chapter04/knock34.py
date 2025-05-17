import spacy

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

# Load the GiNZA model
nlp = spacy.load("ja_ginza")

# Apply dependency parsing
doc = nlp(text)

# Extract predicates where "メロス" is the subject
for token in doc:
    if token.text == "メロス" and token.dep_ == "nsubj":
        predicate = token.head
        print(f"述語: {predicate.text}")