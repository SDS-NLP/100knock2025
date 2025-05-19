verbs_with_stem = []
for sent in sentences:
    if not sent.strip():
        continue
    node = m.parseToNode(sent)
    while node:
        if node.feature.split(',')[0] == '動詞':
            stem = node.feature.split(',')[6]  # 原型の位置
            verbs_with_stem.append((node.surface, stem))
        node = node.next
for v in verbs_with_stem:
    print(f"{v[0]}\t{v[1]}")
# 実行結果:
# 激怒    激怒する
# 除      除く
# 決意    決意する
# わか    わかる
# あ      ある
# 吹      吹く
# 遊      遊ぶ
# 暮      暮す
# 来      来る
# 敏感    敏感である