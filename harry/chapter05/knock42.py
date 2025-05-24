import csv
import requests
import os
import re
import time
from dotenv import load_dotenv

# .envからAPIキー取得
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("❌ '.env' に GROQ_API_KEY が設定されていません。")

# Groq API設定
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

correct = 0
total = 0

# 出力ログファイルを用意（追記モード）
log_path = "output.log"
with open(log_path, "w", encoding="utf-8") as log_file:
    log_file.write("=== LLM 解答ログ ===\n\n")

with open("questions.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader, start=1):
        if i > 30:  # 最初の30問のみ処理
            break

        if len(row) < 6:
            print(f"⚠️ 行 {i} は無視されました（列数不足）")
            continue

        question = row[0]
        choices = row[1:5]
        correct_answer = row[5].strip().upper()

        # プロンプト作成
        prompt = f"{question}\n"
        for idx, label in enumerate(["A", "B", "C", "D"]):
            prompt += f"{label}. {choices[idx]}\n"
        prompt += "正しい選択肢のアルファベットを1文字で答えてください。"

        payload = {
            "model": MODEL,
            "temperature": 0,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        time.sleep(2)

        if response.status_code == 200:
            try:
                full_response = response.json()["choices"][0]["message"]["content"].strip()

                # 正規表現でA〜Dだけ抽出
                # 正規表現で「answer is C」や「答えはC」などを探す
                match = re.search(r"(?:answer\s+is|答えは)[^\w]*([A-D])", full_response, re.IGNORECASE)

                # もし見つからなければ、念のため fallback として最後に出現する A〜D を拾う
                if match:
                    answer_letter = match.group(1).upper()
                else:
                    fallback = re.findall(r"\b([A-D])\b", full_response)
                    answer_letter = fallback[-1].upper() if fallback else "?"

                total += 1
                is_correct = answer_letter == correct_answer
                if is_correct:
                    correct += 1

                print(f"Q{i}: 正解={correct_answer}, 回答={answer_letter}, {'✅正解' if is_correct else '❌不正解'}")

                # ログファイルへの書き込み
                with open(log_path, "a", encoding="utf-8") as log_file:
                    log_file.write(f"【Q{i}】\n")
                    log_file.write(f"問題: {question}\n")
                    log_file.write(f"選択肢: A={choices[0]}, B={choices[1]}, C={choices[2]}, D={choices[3]}\n")
                    log_file.write(f"モデル出力:\n{full_response}\n")
                    log_file.write(f"抽出された選択肢: {answer_letter}\n")
                    log_file.write(f"正解: {correct_answer} → {'✅正解' if is_correct else '❌不正解'}\n")
                    log_file.write("-" * 40 + "\n")
            except Exception as e:
                print(f"❌ 行 {i} のレスポンス解析エラー:", e)
        else:
            print(f"❌ 行 {i} のAPIエラー:", response.status_code, response.text)

# 結果出力
print("\n🎯 結果")
print(f"正解数: {correct} / {total}")
print(f"正解率: {100 * correct / total:.2f}%")