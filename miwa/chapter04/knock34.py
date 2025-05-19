#34. 主述の関係
import spacy

# GiNZAの日本語モデルをロード
nlp = spacy.load("ja_ginza")

text = """メロスは激怒した。必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども、邪悪に対しては、人一倍に敏感であった。"""

doc = nlp(text)

# 主語が「メロス」である述語（動詞）を抽出
for sent in doc.sents:
    for token in sent:
        #  [メロス」という名詞
        # 主語関係（nsubj）である
        if token.text == "メロス" and token.dep_ == "nsubj":
            # 係り先を取得
            pred = token.head
            print(f"文：{sent.text.strip()}")
            print(f"主語：{token.text} → 述語：{pred.text}")
