import cabocha

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

#CaboCha のパーサー（解析器）を生成
parser = cabocha.Parser()
for sentence in text.split('。'):
    if not sentence.strip():#文の終わりなどをスキップ
        continue
    sentence += '。' #.split("。") で削ってしまった「。」をつける
    
    tree = parser.parse(sentence)#係り受け構造の木構造（tree）を生成
    chunks = {}

    for i in range(tree.size()):
        token = tree.token(i)
        if token.chunk:
            chunk = token.chunk
            idx = chunk.link
            chunks[i] = {
                "text": "",
                "dst": idx
            }
    chunk_idx = -1
    for i in range(tree.size()):
        token = tree.token(i)
        if token.chunk:
            chunk_idx += 1
        surface = token.surface
        chunks[chunk_idx]['text'] += surface#チャンクにトークンの表層形を追加（文節を文字列として連結）
    for i in chunks:
        dst = chunk[i]['dst']#チャンクの係り先（どのチャンクに係るか）を取得
        if dst != -1:
            print(f"{chunks[i]['text']}\t{chunks[dst]['text']}")
      




