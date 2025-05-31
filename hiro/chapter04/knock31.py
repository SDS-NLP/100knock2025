from melos import general_list

base_list = []
for sentense in general_list:
    for text in sentense:
        if text["pos"] == "動詞":
            base_list.append(text["base"])
base_verb = set(base_list)
print(base_verb)