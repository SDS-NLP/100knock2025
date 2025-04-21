text="stressed"
inversed_text=""
for i in range(len(text)):
    inversed_text += text[len(text)-i-1]
print(inversed_text)