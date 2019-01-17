"""
"Hi He Lied Because Boron Could Not Oxidize Fluorine.
 New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""


def solve(msg, table, pairs={}):
    xs = map(lambda m: m.replace(".", ""), msg.split())

    for i, x in enumerate(xs, start=1):
        pairs[i] = x[0] if i in table else x[0:2]

    print(pairs)


def solve_(words, table, pairs={}):
    import re
    xs = "".join(re.compile(r"[a-zA-Z ]").findall(words)).split()

    for i, x in enumerate(xs, start=1):
        pairs[i] = x[0] if i in table else x[0:2]

    print(pairs)


given = "Hi He Lied Because Boron Could Not Oxidize Fluorine." \
        " New Nations Might Also Sign Peace Security Clause. Arthur King Can."
heads = {1, 5, 6, 7, 8, 9, 15, 16, 19}

solve(given, heads)
solve_(given, heads)
