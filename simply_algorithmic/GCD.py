"""
Euclidean Algorithm

2 つの自然数 a, b (a ≧ b) について、a の b による剰余を r とすると、
a と b との最大公約数は b と r との最大公約数に等しいという性質が成り立つ。

この性質を利用して、 b を r で割った剰余、
除数 r をその剰余で割った剰余、と剰余を求める計算を逐次繰り返すと、
剰余が 0 になった時の除数が a と b との最大公約数となる。
"""


# Tail recursion
def gcd(a, b):
    if a < 0 or b < 0:
        return "-"

    mx = max(a, b)
    mn = min(a, b)

    if mx % mn == 0:  # exit case
        return mn

    return gcd(mn, mx % mn)  # standard case (pattern)


print(gcd(32, 12))


def gcd_simple(a, b):
    if b == 0:
        return abs(a)
    return gcd_simple(b, a % b)


print(gcd_simple(12, 32))
