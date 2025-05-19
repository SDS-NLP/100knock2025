import MeCab
import os

def parse_text_to_lines(filepath):
    unidic_path = os.path.expanduser("~/unidic-cwj")
    mecabrc_path = "/etc/mecabrc"

    mecab = MeCab.Tagger(
        f"-r {mecabrc_path} -d {unidic_path} "
        "-F '\\t%m\\t%f[7]\\t%f[6]\\t%f[23]\\t%F-[0,1,2,3]\\t%f[4]\\t%f[5]\\t%f[8]\\t%f[9]\\t%f[12]\\t%f[28]\\n' "
        "--unk-format='\\t%m\\t\\t\\t未知語\\t\\t\\n'"
    )
    mecab.parse("")  # 初期化バグ対策

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    output = mecab.parse(text)
    lines = output.strip().split("\n")
    return lines

if __name__ == "__main__":
    base_dir = os.path.expanduser("~/100knock/100knock2025/harry/chapter04")
    text_file = os.path.join(base_dir, "merosu_short.txt")
    lines = parse_text_to_lines(text_file)

    print("🔍 動詞（表層形, 原形）:")
    for line in lines:
        if not line.strip():
            continue
        try:
            cols = line.split()
            surface = cols[0]
            lemma = cols[1]
            pos = cols[4]
            if pos.startswith("動詞"):
                print(f"{surface}")
        except IndexError:
            continue
