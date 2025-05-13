import json

with open("../../../jawiki-country.json") as f:
  data = [json.loads(line) for line in f]

for i in range(len(data)):
  article = data[i]
  if article["title"] == "イギリス":
    uk_article = article
  else:
    continue

article = uk_article["text"]

if __name__ == "__main__":
  print(article)