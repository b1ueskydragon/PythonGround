"""
TODO:
with binary num (bitwise op)
`+` = `XOR` that has carry
0nnn.. == M or 1nnn.. == M
"""


def solve(m, n):
    """
    Brute force.

    a + b = M
    a ^ b = N
    """
    for a in range(1, m + 1):
        for b in range(a, m - a + 1):
            if a + b == m and a ^ b == n:
                print((a, b))


def solve_(m, n):
    """
    O(m)

    b = M - a
    a ^ (M-a) = N
    """
    for a in range(1, m // 2):
        if a ^ (m - a) == n:
            print((a, m - a))


M, N = 300, 10
solve(M, N)
solve_(M, N)
