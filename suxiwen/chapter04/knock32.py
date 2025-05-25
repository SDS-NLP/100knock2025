noun_phrases = []
for sent in sentences:
    if not sent.strip():
        continue
    node = m.parseToNode(sent)
    while node:
        if node.surface == 'の':
            prev_node = node.prev
            next_node = node.next
            if prev_node and next_node:
                prev_pos = prev_node.feature.split(',')[0]
                next_pos = next_node.feature.split(',')[0]
                if prev_pos == '名詞' and next_pos == '名詞':
                    noun_phrase = prev_node.surface + 'の' + next_node.surface
                    noun_phrases.append(noun_phrase)
        node = node.next
print(noun_phrases)
# 実行結果: ['邪智暴虐の王', '村の牧人']