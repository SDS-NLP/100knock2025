"""
knock31: 動詞の原型
textに含まれる動詞と、その原型を全て表示せよ。
"""
import MeCab

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""
tagger = MeCab.Tagger("-r /opt/homebrew/etc/mecabrc -Owakati")

verbs=[]
#文を一語ずつの形態素に分割する、分かち書き
node=tagger.parseToNode(text)

while node:
    if node.feature.startswith("動詞"):       #node.featureは品詞などの情報を含む文字列、動詞かどうか判定
        original_form=node.surface
        base_form=node.feature.split(",")[6]    #基本形
        verbs.append((original_form,base_form)) #基本形をリストに追加
       
       #結果出力
        print(f"動詞:{original_form} 原型:{base_form}")
    node=node.next


