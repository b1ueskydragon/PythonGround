"""
Find the next higher number with same number of set bits.
"""


def _digit(n, d=0):
    while n > 1:
        n //= 2
        d += 1
    return d


def solve(num):
    """
    with shift-op

    0) 10011100
    1) 10111000
    2) 10100011

    0) 1000
    1) 10000
    """
    if num <= 0:
        return

    head = 1 << _digit(n=num)
    body = (num - head) << 1

    if body != 0:
        body = 1 << _digit(n=body)

    print(bin(head + body)[2:])


solve(6)  # 110 (6) -> 1001 (9)
solve(12)  # 1100 (12) -> 10001 (17)
solve(8)  # 1000 (8) -> 10000 (16)
solve(31)  # 11111 (31) -> 101111
solve(156)  # 10011100 (156) -> 10100011 (163)

# 10000000
# 10111000
# 10100011
