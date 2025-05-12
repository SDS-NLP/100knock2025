# count_name_frequency.py

import sys
from collections import Counter

def count_name_frequency(file_path):
    """1列目の名前の出現頻度をカウントし、多い順に表示"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            names = [line.split('\t')[0] for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {file_path}")
        return

    counter = Counter(names)
    sorted_names = counter.most_common()

    print("🧾 出現頻度順（名前: 頻度）")
    for name, count in sorted_names:
        print(f"{name}\t{count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使い方: python count_name_frequency.py ファイル名")
        sys.exit(1)

    file_path = sys.argv[1]
    count_name_frequency(file_path)

# unix command
# cut -f 1 popular-names.txt | sort | uniq -c | sort -nr