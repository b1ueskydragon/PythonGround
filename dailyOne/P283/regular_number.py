def solve(n):
    regular_nums = [1] * n  # pre-set

    count = 1
    while count < n:
        count += 1

    return regular_nums


n = 59
print(solve(n))

"""
x == 2^i * 3^j * 5^k
[x1, x2, ... xN]

len(solve(N)) == N
"""
