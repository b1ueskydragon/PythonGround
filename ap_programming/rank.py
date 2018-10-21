"""
AP 2018 A 3
"""

"""
文字 : 符号 のペア. C : 01 の場合, 0がキー, 1がキーの値
"""
codes: dict = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}


def rank(root, m, r):
    """
    ウェーブレット木で文字の`出現回数`を数える操作.
    (今回`出現位置`は求めない)

    :param root: 根
    :param m: 文字列の長さ
    :param r: 対象の文字列
    :return:
    """
    nodep = root  # 葉のカーソル
    d = 1  # 符号中の左からのビット位置の初期化
    n = m  # 検索対象の文字列の長さを初期化

    while nodep:
        count = 0

        x = 1 << 1  # 桁増やし
        x = x & r
        b = x >> 1  # 桁減らし (キーだけ残す)

        for i in range(1, n + 1):  # range[1, n]
            if b == nodep.key[i]:
                count += 1

        if b == 0:
            nodep = nodep.left
        else:
            nodep = nodep.right

        n -= 1
        d += 1

    return n


def convert(string):
    """
    Convert string to code.
    """
    res = []
    for c in string:
        if c in codes:
            res.append(codes[c])
    return ''.join(res)


target = "CTCGAGAGTA"


# root = convert("CTCGAGAGTA")
# left1 = convert("CCAAA")
# right1 = convert("TGGGT")
# left21 = convert("AAA")
# right22 = convert("CC")
# left23 = convert("GGG")
# right24 = convert("TT")


class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

# TODO Implement Wavelet Matrix(Tree)
