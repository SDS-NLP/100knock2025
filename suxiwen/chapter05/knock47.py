import openai

# OpenAI APIキーの設定
openai.api_key = ''

# 問題46
def generate_senryu(topic="大規模言語モデル"):
    prompt = f"""お題「{topic}」について、ユーモアを交えて川柳を10個作ってください。"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    return response['choices'][0]['message']['content']

# 問題47
def evaluate_senryu(senryu_list):
    joined_senryu = "\n".join([f"{i+1}. {s}" for i, s in enumerate(senryu_list)])
    prompt = f"""以下の川柳10個を、面白さを基準にそれぞれ10段階で評価してください。\n\n{joined_senryu}\n\n出力形式は「番号. 点数（例：1. 7）」としてください。"""
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response['choices'][0]['message']['content']


if __name__ == "__main__":
 
    senryu_text = generate_senryu()
    print("=== 川柳生成 ===")
    print(senryu_text)
    
    # 川柳をリストに変換（改行区切りで単純に分割）
    senryu_list = [line.split(". ", 1)[1] if ". " in line else line for line in senryu_text.strip().split("\n") if line.strip()]
    
    print("\n=== 評価 ===")
    evaluation = evaluate_senryu(senryu_list)
    print(evaluation)