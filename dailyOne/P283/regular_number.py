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

"""
    regular_nums         |  2h |  3h |  5h 
--------------------------------------------
[1, 0, 0, 0, 0, 0, 0, 0] |  1  |  0  |  0
[1, 2, 0, 0, 0, 0, 0, 0] |  1  |  1  |  0 
[1, 2, 3, 0, 0, 0, 0, 0] |  2  |  1  |  0
[1, 2, 3, 4, 5, 0, 0, 0] |  2  |  1  |  1
"""
