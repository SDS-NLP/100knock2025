from knock46 import generate_senryu_list
import openai


with open("key.txt") as f:
    api_key = f.read().strip()

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

senryus = generate_senryu_list()

print("LLMによる川柳評価：\n")

for i, lines in enumerate(senryus, start=1):
    text = "\n".join(lines)
    prompt = f"""以下の川柳を、表現・感情・おもしろさの観点から10点満点で評価してください。

{lines[0]}
{lines[1]}
{lines[2]}

評価は次の形式で出力してください：
評価：X/10　コメント：......"""

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    print(f"{i}. {text.replace(chr(10), ' / ')}")
    print("→", response.choices[0].message.content.strip(), "\n")
