import re

def extract_media_files(text):
    pattern = r'\[\[File:(.*?)\]\]'
    return re.findall(pattern, text, re.IGNORECASE)

media_files = extract_media_files(uk_text)
for file in media_files:
    print(file)