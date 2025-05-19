from melos import general_list

no_list = []
for sentense in general_list:
    for i in range(len(sentense)):
        if sentense[i]["surface"] == "の" and sentense[i-1]["pos"]=="名詞" and sentense[i+1]["pos"]=="名詞":
            no_list.append(sentense[i - 1]["surface"] + "の" + sentense[i + 1]["surface"])
print(no_list)