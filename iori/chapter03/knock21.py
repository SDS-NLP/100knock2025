import knock20
import re
pattern = "\[\[Category:.*?\]\]"
category = re.findall(pattern, knock20.UK_text)
print(category)
