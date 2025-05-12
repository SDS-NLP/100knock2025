from knock20 import article
import re

pattern = r"\[\[Category:(.*?)\]\]"
category = re.findall(pattern, article)
print(category)