from knock20 import article
import re

pattern = "={2,4}.*?={2,4}"
sections = re.findall(pattern, article)
print(sections)
sections_dct = {}

for i in range(len(sections)):
  section = sections[i]
  count = section.count("=")
  n = int(count/2 -1)
  sections_dct[f"{section}"] = n

print(sections_dct)