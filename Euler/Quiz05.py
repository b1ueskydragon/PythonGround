# 特別なピタゴラス数

n = 1000
rng = 500


def pyt(n, rng):
    for c in range(rng):
        for b in range(c):
            for a in range(b):
                target = a * a + b * b
                if (target == c * c and a + b + c == n):
                    print(a * b * c)
                    break


pyt(n, rng)
