"""
knock30:動詞
textに含まれる動詞を全て表示せよ
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
#形態素解析器を作成:Chasen互換のフォーマットを使用
#パスを明示しないとMeCab本体の設定ファイルであるmecabrcが見つからないエラーになる
tagger = MeCab.Tagger("-r /opt/homebrew/etc/mecabrc -Owakati")

verbs=[]
#文を一語ずつの形態素に分割する、分かち書き
node=tagger.parseToNode(text)

while node:
    if node.feature.startswith("動詞"):       #node.featureは品詞などの情報を含む文字列、動詞かどうか判定
        verbs.append(node.surface)            #表層形をリストに追加
    node=node.next

#結果出力
print(verbs)