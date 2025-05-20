"""
knock33:係り受け解析
textに係り受け解析を適用し、係り元と係り先のトークン(形態素や文節などの単位)を
タブ区切り形式で全て抽出せよ
"""
#係り受け解析用の自然言語処理ライブラリ読み込む
import spacy

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""
#GiNZAのモデルをロード:形態素解析・固有表現抽出・係り受け解析などが利用可能になる
nlp=spacy.load("ja_ginza")

#GiNZAによる係り受け解析、解析結果をdocに格納する、文や単語、依存関係の情報をもつオブジェクト　
doc=nlp(text)

#文単位で処理 
for sent in doc.sents:
    #各トークン(単語)に対する係り受け解析
    for token in sent:
        #係り元と係り先をタブ区切りで出力
        #token.text:現在の単語(係り元)
        #token.head.text:その単語の係り先の単語
        #係り元!=係り先の時のみ出力
        if  token.text !=token.head.text:
              print(f"{token.text}\t{token.head.text}")