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

# Extract and print dependency relations
for token in doc:
    print(f"{token.text}\t{token.head.text}")