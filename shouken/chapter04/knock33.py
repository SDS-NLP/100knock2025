import CaboCha

with open("merosu.txt", encoding="utf-8") as f:
    text = f.read()

parser = CaboCha.Parser()

tree = parser.parse(text)

# 係り受け情報をたどる
sent = tree.toString(CaboCha.FORMAT_TREE)
lines = sent.splitlines()

chunks = []
chunk = {"tokens": [], "dst": -1}

# 文節情報を構造化
for line in lines:
    if line == "EOS":
        if chunk["tokens"]:
            chunks.append(chunk)
        break
    elif line.startswith("*"):
        if chunk["tokens"]:
            chunks.append(chunk)
        parts = line.split()
        dst = int(parts[2].rstrip("D"))
        chunk = {"tokens": [], "dst": dst}
    else:
        token = line.split("\t")[0]
        chunk["tokens"].append(token)

# 係り受けペアを表示
for i, chunk in enumerate(chunks):
    dst = chunk["dst"]
    if dst != -1 and dst < len(chunks):
        src_phrase = "".join(chunk["tokens"])
        dst_phrase = "".join(chunks[dst]["tokens"])
        print(f"{src_phrase}\t{dst_phrase}")
