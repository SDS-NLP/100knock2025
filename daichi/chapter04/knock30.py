import MeCab

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

tagger = MeCab.Tagger()
tagger.parse("")  # セグフォ対策

node = tagger.parseToNode(text) # 形態素解析の実行
# 形態素解析の結果を1行ずつ処理
while node:
    features = node.feature.split(",") # 形態素の特徴をカンマで分割
    if features[0] == "動詞": # 品詞が動詞の場合
        print(node.surface) # 動詞の表層形を出力
    node = node.next # 次の形態素に移動
