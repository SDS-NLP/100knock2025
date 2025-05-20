import re

def extract_category_names(text):
    pattern = r'\[\[Category:(.*?)(?:\|.*?)?\]\]'
    return re.findall(pattern, text)

category_names = extract_category_names(uk_text)
for name in category_names:
    print(name)