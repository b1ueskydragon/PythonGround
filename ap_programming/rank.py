"""
AP 2018 A 3
"""


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
