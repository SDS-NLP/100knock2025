import os
from dotenv import load_dotenv
from google import genai
import random
import re
from google.genai.types import GenerateContentConfig

load_dotenv()

client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

# 適当なお題リスト
topics = [
    "プログラミング",
    "コーヒー",
    "雨の日",
    "通勤電車",
    "リモートワーク",
    "スマートフォン",
    "猫",
    "お正月",
    "桜",
    "夏祭り"
]

# ランダムにお題を選択
selected_topic = random.choice(topics)
print(f"お題: {selected_topic}")
print("=" * 30)

# 川柳を10個作成するプロンプト
prompt = f"""
お題「{selected_topic}」で川柳を10個作成してください。
各川柳には番号を付けて、以下の形式で出力してください：

1. ○○○○○（5音）
   ○○○○○○○（7音）
   ○○○○○（5音）

2. ○○○○○（5音）
   ○○○○○○○（7音）
   ○○○○○（5音）

...（10個まで）

ユーモアや風刺を込めた川柳を作成してください。
"""

# システム指示を設定
config = GenerateContentConfig(
    system_instruction=[
        "あなたは経験豊かな俳句・川柳の専門家です。",
        "5-7-5の音律（語数ではない）を正確に守り、季語や心情を巧みに表現する才能があります。",
        "日本の伝統的な川柳の技法を理解し、現代的な感性も取り入れることができます。",
        "ユーモアや風刺、人生の機微を短い言葉で表現することが得意です。",
        "音数を正確に数え、美しい日本語で川柳を作成してください。"
    ]
)

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-05-20",
    contents=prompt,
    config=config
)

print("【生成された川柳】")
print(response.text)
print("\n" + "=" * 50)

# 川柳を抽出する関数
def extract_senryu(text):
    """生成されたテキストから川柳を抽出する"""
    senryus = []
    lines = text.split('\n')
    current_senryu = []
    current_number = None
    
    for line in lines:
        line = line.strip()
        if not line:
            if current_senryu and len(current_senryu) == 3:
                senryus.append({
                    'number': current_number,
                    'senryu': '\n'.join(current_senryu)
                })
            current_senryu = []
            current_number = None
            continue
            
        # 番号で始まる行を検出
        number_match = re.match(r'^(\d+)\.?\s*(.+)', line)
        if number_match:
            # 前の川柳を保存
            if current_senryu and len(current_senryu) == 3:
                senryus.append({
                    'number': current_number,
                    'senryu': '\n'.join(current_senryu)
                })
            current_number = number_match.group(1)
            current_senryu = [number_match.group(2)]
        elif current_senryu and len(current_senryu) < 3:
            current_senryu.append(line)
    
    # 最後の川柳を保存
    if current_senryu and len(current_senryu) == 3:
        senryus.append({
            'number': current_number,
            'senryu': '\n'.join(current_senryu)
        })
    
    return senryus

# 川柳を評価する関数
def evaluate_senryu(senryu_text, topic):
    """川柳の面白さを10段階で評価する"""
    evaluation_prompt = f"""
以下の川柳をお題「{topic}」に対する作品として評価してください。

川柳:
{senryu_text}

評価基準:
1. ユーモア・面白さ（4点満点）
2. お題との関連性（3点満点）
3. 川柳としての技法・表現力（3点満点）

合計10点満点で評価し、以下の形式で回答してください：

【評価点】: X/10点
【評価理由】: 具体的な評価理由を簡潔に記述
"""
    
    evaluation_config = GenerateContentConfig(
        system_instruction=[
            "あなたは川柳の専門評価者です。",
            "ユーモア、表現技法、お題との関連性を総合的に評価してください。",
            "公平で建設的な評価を心がけてください。",
            "評価は1-10の整数で行い、理由も簡潔に述べてください。"
        ]
    )
    
    try:
        eval_response = client.models.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents=evaluation_prompt,
            config=evaluation_config
        )
        return eval_response.text
    except Exception as e:
        return f"評価エラー: {str(e)}"

# 川柳を抽出
senryus = extract_senryu(response.text)

print("【川柳評価結果】")
print("=" * 50)

total_score = 0
evaluated_count = 0

for senryu_data in senryus:
    print(f"\n川柳 {senryu_data['number']}:")
    print(senryu_data['senryu'])
    print("-" * 30)
    
    # 評価を実行
    evaluation = evaluate_senryu(senryu_data['senryu'], selected_topic)
    print(evaluation)
    
    # 評価点を抽出して集計
    score_match = re.search(r'(\d+)/10', evaluation)
    if score_match:
        score = int(score_match.group(1))
        total_score += score
        evaluated_count += 1
    
    print("=" * 50)

# 平均評価を表示
if evaluated_count > 0:
    average_score = total_score / evaluated_count
    print(f"\n【総合評価】")
    print(f"評価対象川柳数: {evaluated_count}個")
    print(f"平均評価点: {average_score:.1f}/10点")
    print(f"お題: {selected_topic}")