'''
暗号文

与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''


def cipher(target_stc):
    encrypt_stc = ""
    for s in target_stc:
        if not s.isalnum():
            encrypt_stc += s.replace(s, "@")
        else:
            encrypt_stc += s
    return encrypt_stc


stc = "hello, b1ueskydragon!"
print(cipher(stc))
