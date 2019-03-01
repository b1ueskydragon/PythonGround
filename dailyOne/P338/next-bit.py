"""
Find the next higher number with same number of set bits.
"""


def solve(num):
    """
    with shift-op

    0) 10011100
    1) 100111000
    2) 101000000
    3) 10100000
    4) 10100011
    """

    num <<= 1

    b1 = bin(num)[2:]

    print(b1)


solve(6)  # 0110 (6) -> 1001 (9)
solve(12)  # 1100 (12) -> 10001 (17)
solve(8)  # 1000 (8) -> 10000 (16)
solve(156)  # 10011100 (156) -> 10100011 (163)
