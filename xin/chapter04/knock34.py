import CaboCha
import knock30
text = knock30.text

# CaboChaの初期化
parser = CaboCha.Parser()

# 解析結果を取得
tree = parser.parse(text)

# 「メロス」を主語とする述語を抽出
for i in range(tree.chunk_size()):
    chunk = tree.chunk(i)
    tokens = [tree.token(j).surface for j in range(chunk.token_pos, chunk.token_pos + chunk.token_size)]
    
    # 「メロス」が含まれる文節を探す
    if "メロス" in tokens and chunk.link != -1:  
        dst_chunk = tree.chunk(chunk.link)  # 係り先の文節を取得
        pred_tokens = [tree.token(j).surface for j in range(dst_chunk.token_pos, dst_chunk.token_pos + dst_chunk.token_size)]
        
        # 述語を表示
        print(" ".join(pred_tokens))