import json

with open("./hiro/chapter03/jawiki-country.json") as f:
    article_list = [json.loads(line) for line in f]

    for i in range(len(article_list)):
        if article_list[i]["title"] == "イギリス":
            uk_article_txt = article_list[i]["text"]
            break

if __name__ == "__main__":
            print(uk_article_txt)