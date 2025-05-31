from melos import general_list

suf_list = []
for sentense in general_list:
    for text in sentense:
        if text["pos"] == "動詞":
            suf_list.append(text["surface"])
verb = set(suf_list)
print(verb)