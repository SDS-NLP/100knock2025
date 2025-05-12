import knock20
import re
pattern = "\[\[Category:(.*?)(?:\|.*?|)\]\]"
result = re.findall(pattern, knock20.UK_text)

print(result)
