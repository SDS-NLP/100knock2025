# 単語（形態素）の出現頻度を求め、出現頻度の高い20語とその出現頻度を表示せよ。

with open('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter04/kokoro.txt', 'r', encoding='utf-8') as f:
    texts = []
    text_flag = 0
    for s_line in f:
        if len(s_line.strip()) < 4 and len(s_line.strip()) != 0:
            continue
        if len(s_line.strip()) == 0:
            if text_flag == 0:
                text_flag = 1
                text = ''
                continue
            else:
                text_flag = 0
                texts.append(text)
                continue
        if text_flag == 1:
            text += s_line.strip()

if __name__ == '__main__':

    import MeCab

    mecab = MeCab.Tagger('-Ochasen')

    numcount = {}

    for text in texts:
        node = mecab.parseToNode(text)
        while node:
            if node.surface not in numcount:
                numcount[node.surface] = 0
            numcount[node.surface] += 1
            node = node.next
    # 出現頻度の高い上位20語とその出現頻度を表示
    for i, (word, count) in enumerate(sorted(numcount.items(), key=lambda x: x[1], reverse=True)):
        if i >= 20:
            break
        print(f"{i+1}位 単語：{word} 出現頻度：{count}")
