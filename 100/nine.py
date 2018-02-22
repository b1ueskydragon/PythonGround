"""
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替える
"""

import random as rd


def typoglycemia(words):
    output = []
    for word in words.split(" "):  # 長さ4超過の単語は並び替え
        if len(word) > 4:
            tmp_body = list(word[1:-1])
            rd.shuffle(tmp_body)
            word = word[0] + "".join(tmp_body) + word[-1]
        output.append(word)
    return " ".join(output)


words = "I couldn't believe that I could actually understand what I was reading" \
        " : the phenomenal power of the human mind ."

print(typoglycemia(words))
