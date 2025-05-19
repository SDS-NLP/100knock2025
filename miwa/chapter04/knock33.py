#33. 係り受け解析
import spacy
import ginza

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

nlp = spacy.load("ja_ginza")
doc = nlp(text)

# 係り受けを1行ずつ「係り元語彙」「係り先語彙」のタブ区切りで出力
for sent in doc.sents:
    for token in sent:
        if token.head == token:
            continue  # ルートは除外（または出力してもOK）
        print(f"{token.text}\t{token.head.text}")