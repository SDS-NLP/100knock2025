import re

def extract_category_lines(text):
    pattern = r'^\[\[Category:.+?\]\]$'
    return [line for line in text.split('\n') if re.match(pattern, line)]

category_lines = extract_category_lines(uk_text)
for line in category_lines:
    print(line)