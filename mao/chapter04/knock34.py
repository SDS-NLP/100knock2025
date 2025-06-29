"""
knock34: 主述の関係
textにおいて、「メロス」が主語であるときの述語を抽出せよ。
"""
import spacy

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""
answer=[] #結果格納用

nlp=spacy.load("ja_ginza")
doc=nlp(text)

for sent in doc.sents:
    for token in sent:
        #対象の主語が「メロス」であるかを確認
        #token.deq_:依存関係ラベル
        #nsubj:主語、obj:目的語、nsubj:pass:受動態の主語
        if token.text=="メロス" and token.dep_ in ("nsubj","nsubj:pass"):
            head=token.head
            if head.dep_ in ("ROOT"): #ROOT:各文の中心
                answer.append(token.head.text)

#結果表示
print(answer)
