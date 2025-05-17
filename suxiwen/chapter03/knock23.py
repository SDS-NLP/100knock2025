import re

def extract_sections(text):
    pattern = r'^=+ (.*?) =+$'
    sections = []
    for line in text.split('\n'):
        match = re.match(pattern, line)
        if match:
            level = len(match.group(0).split()[0]) - 1  # 等号数-1でレベル
            name = match.group(1)
            sections.append((level, name))
    return sections

sections = extract_sections(uk_text)
for level, name in sections:
    print(f"レベル: {level}, セクション名: {name}")