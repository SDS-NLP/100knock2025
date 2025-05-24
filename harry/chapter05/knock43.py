import csv
import requests
import os
import re
import sys
from dotenv import load_dotenv
import time

# .env 読み込み
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("❌ GROQ_API_KEY が .env に設定されていません。")

# コマンドライン引数から temperature を取得
if len(sys.argv) != 2:
    print("Usage: python evaluate_temp.py <temperature>")
    sys.exit(1)

try:
    temperature = float(sys.argv[1])
except ValueError:
    print("❌ temperature は数値で指定してください（例: 0.0, 0.7, 1.0）")
    sys.exit(1)

# API 設定
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# ログファイルの準備
log_path = f"log_temperature_{temperature}.txt"
with open(log_path, "w", encoding="utf-8") as log_file:
    log_file.write(f"=== LLM 解答ログ（temperature={temperature}）===\n\n")

correct = 0
total = 0

with open("questions.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader, start=1):
        if i > 20:  # 20問まで処理
            break

        if len(row) < 6:
            print(f"⚠️ 行 {i} は無視されました（列数不足）")
            continue

        question = row[0]
        choices = row[1:5]
        correct_answer = row[5].strip().upper()

        prompt = f"{question}\n"
        for idx, label in enumerate(["A", "B", "C", "D"]):
            prompt += f"{label}. {choices[idx]}\n"
        prompt += "正しい選択肢のアルファベットを1文字で答えてください。"

        payload = {
            "model": MODEL,
            "temperature": temperature,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        time.sleep(2)

        if response.status_code == 200:
            try:
                full_response = response.json()["choices"][0]["message"]["content"].strip()

                # 抽出：答えは A〜D のうち最後に宣言されたもの
                match = re.search(r"(?:answer\s+is|答えは)[^\w]*([A-D])", full_response, re.IGNORECASE)
                if match:
                    answer_letter = match.group(1).upper()
                else:
                    fallback = re.findall(r"\b([A-D])\b", full_response)
                    answer_letter = fallback[-1].upper() if fallback else "?"

                total += 1
                is_correct = answer_letter == correct_answer
                if is_correct:
                    correct += 1

                print(f"\nQ{i}: 正解={correct_answer}, 回答={answer_letter}, {'✅正解' if is_correct else '❌不正解'}")

                with open(log_path, "a", encoding="utf-8") as log_file:
                    log_file.write(f"【Q{i}】\n")
                    log_file.write(f"問題: {question}\n")
                    log_file.write(f"選択肢: A={choices[0]}, B={choices[1]}, C={choices[2]}, D={choices[3]}\n")
                    log_file.write(f"モデル出力:\n{full_response}\n")
                    log_file.write(f"抽出された選択肢: {answer_letter}\n")
                    log_file.write(f"正解: {correct_answer} → {'✅正解' if is_correct else '❌不正解'}\n")
                    log_file.write("-" * 40 + "\n")

            except Exception as e:
                print(f"❌ 行 {i} の解析エラー:", e)
        else:
            print(f"❌ 行 {i} のAPIエラー:", response.status_code, response.text)

# 結果出力
print("\n🎯 結果")
print(f"正解数: {correct} / {total}")
print(f"正解率: {100 * correct / total:.2f}%")