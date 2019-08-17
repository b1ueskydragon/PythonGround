# (1)
def read(x, a3, a2, a1, a0):
    """
    x^3 - 3x^2 - x + 3 = 0 の解の一つを求める (実解 3, 1, -1)

    @:param x 解の予測値
    @:param a3, a2, a1, a0 係数
    """
    b2 = 3.0 * a3
    b1 = 2.0 * a2
    b0 = a1

    for i in range(1, 101):
        f = ((a3 * x + a2) * x + a1) * x + a0
        d = (b2 * x + b1) * x + b0
        print(i, "th:", x, f, d)
        x = x - f / d  # 7th 以降桁あふれる


read(2.5, 1, -3, -1, 3)
