#55. アナロジータスクでの正解率
import os
import pickle
from collections import defaultdict
from knock50 import model
from tqdm import tqdm  

#sなしで新しくやってみる
path = "questions-words.txt"
pkl_gram = "result_grammer.pkl"
pkl_mean = "result_meaning.pkl"

# 辞書があれば読み込む　なければ計算して保存する
#処理がとても遅かったので何度もやりたくないから
#終わりが見えなくて不安だったので進捗状況を表示できるtqdmを使った

#辞書が存在する場合
if os.path.exists(pkl_gram) and os.path.exists(pkl_mean):
    with open(pkl_gram, "rb") as f:
        result_grammer = pickle.load(f)
    with open(pkl_mean, "rb") as f:
        result_meaning = pickle.load(f)
    print("結果を読み込みました")

#辞書が存在しない場合
else:
    results_meaning = defaultdict(list)
    results_grammer = defaultdict(list)

    #セクション見出し行がgram~から始まっていたら文法的アナロジー
    #現在のセクションがgramを含むかどうか判定するための旗
    current_section_has_gram = False 

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in tqdm(lines, desc="アナロジー演算中"):
        line = line.strip()

        #セクション見出し行に対する処理
        if line.startswith(":"):
            #"gram" in line の結果(True or False)をcurrent_section_has_gramに代入
            current_section_has_gram = "gram" in line
            continue

        fields = line.split()
        if len(fields) < 4: #フォーマットが一致していない行があればスキップ
            continue

        try:
            result = model.most_similar(positive=[fields[1], fields[2]], negative=[fields[0]],topn=1)[0]

            if current_section_has_gram:
                results_grammer[f"{fields[1]} - {fields[0]} + {fields[2]}:"].append((result, fields[3]))
            else:
                results_meaning[f"{fields[1]} - {fields[0]} + {fields[2]}:"].append((result, fields[3]))

        except KeyError:
            continue

    # 保存
    with open(pkl_gram, "wb") as f:
        pickle.dump(results_grammer, f)
    with open(pkl_mean, "wb") as f:
        pickle.dump(results_meaning, f)
    print("結果を保存しました")

#帰ってきた結果を見て
# リストの値が２値になってしまっているところの最後の要素を削除
for i, key in enumerate(result_meaning):
    if len(result_meaning[key]) > 1:
        result_meaning[key].pop()
for i, key in enumerate(result_grammer):
    if len(result_grammer[key]) > 1:
        result_grammer[key].pop()

# 上書き保存
with open(pkl_mean, "wb") as f:
    pickle.dump(result_meaning, f)
with open(pkl_mean, "wb") as f:
    pickle.dump(result_meaning, f)

# 正解率を計算する関数
def calculate_accuracy(results_dict):
    total = 0
    correct = 0
    for _, value_list in results_dict.items():
        for result, correct_word in value_list:
            predicted_word = result[0]
            if predicted_word.lower() == correct_word.lower(): #大文字小文字を区別しない
                correct += 1
            total += 1
    accuracy = correct / total if total > 0 else 0
    return accuracy, correct, total

# 正解率を表示
acc_gram, correct_gram, total_gram = calculate_accuracy(result_grammer)
print(f"文法的アナロジーの正解率: {acc_gram:.2%} ({correct_gram}/{total_gram})")

acc_mean, correct_mean, total_mean = calculate_accuracy(result_meaning)
print(f"意味的アナロジーの正解率: {acc_mean:.2%} ({correct_mean}/{total_mean})")

# 最初の15件を表示
#print("文法的アナロジー15件")
#for i, (key, value) in enumerate(result_grammer.items()):
    #if i >= 15:
        #break
    #print(f"{key} → {value}")

#print("意味的アナロジー15件")
#for i, (key, value) in enumerate(result_meaning.items()):
    #if i >= 15:
        #break
    #print(f"{key} → {value}")