import re
import knock20

section = {}

# セクションの抽出とレベルの計算
pattern = r"^(={2,})\s*(.+?)\s*\1$"
for match in re.finditer(pattern, knock20.uk_text, re.MULTILINE):
    level = len(match.group(1)) - 1  # '=' の数からレベルを計算
    title = match.group(2)
    section[title] = level

# 結果の出力
for title, level in section.items():
    print(f"レベル{level}: {title}")
