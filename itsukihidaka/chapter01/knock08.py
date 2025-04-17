# 与えられた文字列の各文字を、以下の仕様で変換する関数cipherを実装せよ。
# 英小文字ならば (219 - 文字コード) のASCIIコードに対応する文字に置換
# その他の文字はそのまま出力
# この関数を用い、英語のメッセージを暗号化・復号化せよ。

def cipher(text):
    return ''.join(chr(219 - ord(c)) if c.islower() else c for c in text)

print(f'暗号化: {cipher("Hello, World!")}')
print(f'復号化: {cipher(cipher("Hello, World!"))}')