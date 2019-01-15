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


def solve__(m, n):
    """"
    bitwise op

    a + b = M
    a ^ b = N

    a + b = (a ^ b) + ((a & b) << 1)
    M     = N       + 2(a & b)
    a & b = (M - N) // 2
    """


M, N = 300, 10
# solve(M, N)
solve_(M, N)
solve__(M, N)
