def solve(n):
    """
    Dijkstra's Hamming numbers
     - 1 に 2, 3, 5 を k回 (k>=0) かけ算して得られる数

    O(n)
    """
    nums = [1] * n  # pre-set
    i2, i3, i5 = 0, 0, 0  # smallest indices of the array - multiplying by each prime factors

    for i in range(1, n):
        num = min(2 * nums[i2], 3 * nums[i3], 5 * nums[i5])
        nums[i] = num

        if num % 2 == 0:
            i2 += 1
        if num % 3 == 0:
            i3 += 1
        if num % 5 == 0:
            i5 += 1

    return nums


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
