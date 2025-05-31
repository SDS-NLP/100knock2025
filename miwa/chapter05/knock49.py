#49. トークン化
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("API_KEY")

client = genai.Client(api_key=key)

prompt = """

吾輩は猫である。名前はまだ無い。
どこで生れたかとんと見当がつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。しかもあとで聞くとそれは書生という人間中で一番獰悪な種族であったそうだ。この書生というのは時々我々を捕えて煮て食うという話である。しかしその当時は何という考もなかったから別段恐しいとも思わなかった。ただ彼の掌に載せられてスーと持ち上げられた時何だかフワフワした感じがあったばかりである。掌の上で少し落ちついて書生の顔を見たのがいわゆる人間というものの見始であろう。この時妙なものだと思った感じが今でも残っている。第一毛をもって装飾されべきはずの顔がつるつるしてまるで薬缶だ。その後猫にもだいぶ逢ったがこんな片輪には一度も出会わした事がない。のみならず顔の真中があまりに突起している。そうしてその穴の中から時々ぷうぷうと煙を吹く。どうも咽せぽくて実に弱った。これが人間の飲む煙草というものである事はようやくこの頃知った。

"""

total_tokens = client.models.count_tokens(
    model="gemini-2.0-flash", contents=prompt
)
print("total_tokens: ", total_tokens)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt, 
)
print(response.usage_metadata)

## 結果
# total_tokens:  total_tokens=272 cached_content_token_count=None]
#
# cache_tokens_details=None cached_content_token_count=None candidates_token_count=267
# candidates_tokens_details=[ModalityTokenCount(modality=<MediaModality.TEXT: 'TEXT'>, token_count=267)] 
# prompt_token_count=252 
# prompt_tokens_details=[ModalityTokenCount(modality=<MediaModality.TEXT: 'TEXT'>, token_count=252)] 
# thoughts_token_count=None 
# tool_use_prompt_token_count=None 
# tool_use_prompt_tokens_details=None 
# total_token_count=519 traffic_type=None