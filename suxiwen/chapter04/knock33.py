import spacy  # 自然言語処理ライブラリのspacyをインポート

# 日本語解析用の事前学習モデル「ja_ginza」を読み込み（形態素解析・係り受け解析等をサポート）
nlp = spacy.load("ja_ginza")

# 解析対象のテキスト（複数文を含む日本語文章）
text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

# テキストを解析（形態素解析・品詞タグ付け・係り受け関係抽出を一括実行）
doc = nlp(text)

# 出力のヘッダーを表示（タブ区切り形式）
print("係り元\t助詞\t係り先")

# 文ごとに処理を実行
for sent in doc.sents:
    # 文内の各トークン（単語）を1つずつ処理
    for token in sent:
        # 処理対象を「助詞」または「接続詞」に限定（係り受けの橋渡し役となる品詞）
        if token.pos_ in ["助詞", "接続詞"]:
            
            # 【係り元】：助詞の左側（修飾側）にある名詞/副詞/連体詞を探索
            # token.lefts：トークンの左側にある修飾語（子要素）のリスト
            # 最も近い名詞/副詞/連体詞を優先的に取得（見つからない場合は助詞自身を暫定値とする）
            src = ""
            for child in token.lefts:
                if child.pos_ in ["名詞", "副詞", "連体詞"]:
                    src = child.text  # 係り元を設定
                    break  # 最も近い有効トークンを見つけたらループ終了
            if not src:
                src = token.text  # 係り元が見つからない場合、助詞自身を係り元とする
            
            # 【係り先】：助詞が依存する先のトークン（主に動詞/形容詞などの述語）
            # token.head：係り受け関係において、このトークンが依存する親トークン
            dest = token.head.text if token.head.text != token.text else ""  # 自己参照を避ける
            
            # 無効な記号（「、」「。」）を除外し、有効なデータのみ出力
            if src and dest and token.text not in "、。":
                print(f"{src}\t{token.text}\t{dest}")  # タブ区切りで結果を出力