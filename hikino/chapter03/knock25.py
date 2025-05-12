from knock20 import article
import re

pattern = r"基礎情報 (.*?<references/>)"
base_info = re.findall(pattern, article, flags=re.DOTALL)
base_info = base_info[0]

pattern2 = r"\|(.*?)(?: = | =)(.*?)\n"
items = re.findall(pattern2, base_info)

results = {}

for i in range(len(items)):
  tpl = items[i]
  title = tpl[0]
  content = tpl[1]
  results[f"{title}"] = content

print(results)