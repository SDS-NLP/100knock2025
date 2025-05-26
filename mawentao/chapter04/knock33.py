#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#terminalに　cabocha -f1 /Users/niaomuqing/100knock2025/melos.txt > /Users/niaomuqing/100knock2025/parsed.txt

chunks = {}
chunk_id = -1

with open('/Users/niaomuqing/100knock2025/parsed.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
        #（if line == '':）とも書ける
            continue
        if line == 'EOS':
            for i, chunk in chunks.items():
                dst = chunk['dst']
                if dst != -1 and dst in chunks:
                    src = ''.join(chunk['tokens'])
                    dst_text = ''.join(chunks[dst]['tokens'])
                    print(f"{src}\t{dst_text}")
            chunks = {}
            chunk_id = -1
        elif line.startswith('*'):
            # 文節行：* 
            cols = line.split(' ')
            chunk_id += 1
            dst = int(cols[2][:-1]) 
            chunks[chunk_id] = {'tokens': [], 'dst': dst}
        else:
            # 形態素行：表層形\t品詞情報
            surface = line.split('\t')[0]
            chunks[chunk_id]['tokens'].append(surface)

