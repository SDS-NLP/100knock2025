for sent in sentences:
    if 'メロス' in sent:
        node = m.parseToNode(sent)
        while node:
            if node.surface == 'メロス':
                current = node.next
                while current:
                    if current.feature.split(',')[0] == '動詞':
                        print(current.surface)
                    current = current.next
            node = node.next
# 実行結果: ['激怒', 'わか', 'あ']