#ファイルサイズがデカすぎるので、最初の１０問だけ用いる

from gensim.models import KeyedVectors

model_path = 'GoogleNews-vectors-negative300.bin'
analogy_file = 'questions-words.txt'

print("Loading word vectors...")
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("Word vectors loaded.")

# 正解数と総数の初期化
correct = 0
total = 0

# セクション名（optional）
current_section = None

with open(analogy_file, 'r') as f:
    line_count = 0
    for line in f:
        line = line.strip()
        if line.startswith(':'):
            current_section = line[2:].strip()
            continue

        if line_count >= 10:
            break  # 最初の10行だけ処理

        words = line.split()
        if len(words) != 4:
            continue

        if all(word in model for word in words):
            predicted = model.most_similar(
                positive=[words[1], words[2]],
                negative=[words[0]],
                topn=1
            )[0][0]

            if predicted.lower() == words[3].lower():
                correct += 1
            total += 1
            line_count += 1

# 結果表示
if total > 0:
    accuracy = correct / total * 100
    print(f"\nAccuracy on first 10 analogy questions: {accuracy:.2f}% ({correct}/{total})")
else:
    print("\nNo valid analogy questions found in the first 10 lines.")
