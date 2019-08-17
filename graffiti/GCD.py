"""
Euclidean Algorithm

2 つの自然数 a, b (a ≧ b) について、a の b による剰余を r とすると、
a と b との最大公約数は b と r との最大公約数に等しいという性質が成り立つ。

この性質を利用して、 b を r で割った剰余、
除数 r をその剰余で割った剰余、と剰余を求める計算を逐次繰り返すと、
剰余が 0 になった時の除数が a と b との最大公約数となる。
"""


# Tail recursion
# if a < b, swap automatically
def gcd(a, b):
    if a % b == 0:  # exit case
        return b

    return gcd(b, a % b)  # standard case (pattern)


print(gcd(12, 32))


# Tail recursion
def gcd_a(a, b):
    if b == 0:
        return abs(a)
    return gcd_a(b, a % b)


print(gcd_a(12, 32))
