import requests
from dotenv import load_dotenv
import os
load_dotenv() 
API_KEY = os.getenv("GROQ_API_KEY")

API_URL = "https://api.groq.com/openai/v1/chat/completions"


prompt = """
吾輩は猫である。名前はまだ無い。

どこで生れたかとんと見当がつかぬ。
何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。
吾輩はここで始めて人間というものを見た。
しかもあとで聞くとそれは書生という人間中で一番獰悪な種族であったそうだ。
この書生というのは時々我々を捕えて煮て食うという話である。
しかしその当時は何という考もなかったから別段恐しいとも思わなかった。
ただ彼の掌に載せられてスーと持ち上げられた時何だかフワフワした感じがあったばかりである。
掌の上で少し落ちついて書生の顔を見たのがいわゆる人間というものの見始であろう。
この時妙なものだと思った感じが今でも残っている。
第一毛をもって装飾されべきはずの顔がつるつるしてまるで薬缶だ。
その後猫にもだいぶ逢ったがこんな片輪には一度も出会わした事がない。
のみならず顔の真中があまりに突起している。
そうしてその穴の中から時々ぷうぷうと煙を吹く。どうも咽せぽくて実に弱った。
これが人間の飲む煙草というものである事はようやくこの頃知った。
"""


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

payload = {
    "model": "meta-llama/llama-4-scout-17b-16e-instruct",
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 1,
    "temperature": 0.0
}

response = requests.post(API_URL, headers=headers, json=payload)


result = response.json()
usage = result.get("usage", {})
prompt_tokens = usage.get("prompt_tokens", "?")
completion_tokens = usage.get("completion_tokens", "?")
total_tokens = usage.get("total_tokens", "?")

print(f"プロンプトのトークン数: {prompt_tokens}")
print(f"応答のトークン数: {completion_tokens}")
print(f"合計トークン数: {total_tokens}")