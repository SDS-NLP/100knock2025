import os
import re
import statistics
from dotenv import load_dotenv
import google.generativeai as genai

# .envからAPIキー取得
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# 使用するモデル（軽量で速いもの）
model = genai.GenerativeModel("models/gemini-1.5-flash")

# 評価対象の川柳リスト（例: AI をテーマとした句）
senryu_list = [
    "AIが描く　未来の絵は　まだ白紙",
    "知恵の泉　AI深く　潜りゆく",
    "便利なAI　人の仕事は　どうなるやら",
    "AI先生　優しく教えて　未来へ導く",
    "冷たい画面　AIの言葉　心に響く",
    "夢を語る　AIと共に　夜空見上げる",
    "進化続ける　AIの瞳　光放つ",
    "創造の翼　AI広げ　空を飛ぶ",
    "頼りになる　AIのパートナー　共に生きる",
    "答えは一つ　AIは言う　その先へは"
]

# プロンプトテンプレート
def make_prompt(senryu_list):
    poems = "\n".join(f"- {line}" for line in senryu_list)
    return f"""以下の川柳を、面白さの観点から10段階（1〜10点）で評価してください。
評価の基準：ユーモア、表現の意外性、言葉選びの巧みさ。
各川柳の得点のみを以下のように番号とともに明示してください（理由は不要です）：

{poems}

出力形式（例）:
1. 7
2. 5
...
"""

# 正規表現でスコアを抽出
def extract_scores(text):
    pattern = re.compile(r"\b\d+\.\s*(\d{1,2})\b")
    return [int(match.group(1)) for match in pattern.finditer(text) if 1 <= int(match.group(1)) <= 10]

# 複数回評価を行い、分散を算出
all_scores = []
n_trials = 5

print(f"川柳評価を {n_trials} 回繰り返し、スコアの分散を測定します...\n")

for i in range(n_trials):
    prompt = make_prompt(senryu_list)
    response = model.generate_content(prompt)
    scores = extract_scores(response.text)

    if len(scores) != len(senryu_list):
        print(f"評価 {i+1} 回目: スコア抽出に失敗しました。取得数={len(scores)}")
        continue

    print(f"評価 {i+1} 回目スコア: {scores}")
    all_scores.append(scores)

# 川柳ごとに分散を計算
if all_scores:
    poem_scores_transposed = list(zip(*all_scores))  # 転置して各川柳ごとのスコアリストに
    print("\n📊 川柳ごとのスコア分散:")
    for idx, scores in enumerate(poem_scores_transposed, start=1):
        var = statistics.variance(scores) if len(scores) > 1 else 0
        print(f"{idx}. 分散 = {var:.2f} （スコア履歴: {scores}）")
