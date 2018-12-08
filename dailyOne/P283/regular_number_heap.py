"""
very naive solution is
  O(N^3 * logN), logN for sorting ::


def naive(n):
    twos = [2 ** _ for _ in range(n)]
    threes = [3 ** _ for _ in range(n)]
    fives = [5 ** _ for _ in range(n)]

    nums = set()

    for two in twos:
        for three in threes:
            for five in fives:
                nums.add(two * three * five)

    return sorted(nums)[:n]

"""

import heapq


def solve(n):
    """
    O(N * logN)
    :param n:
    :return:
    """
    nums = [1]
    prev = 0  # the number that yielded last
    count = 0

    while count < n:  # until yielding N nums
        curr = heapq.heappop(nums)  # pop the smallest item
        if curr > prev:
            yield curr

            prev = curr
            count += 1

            heapq.heappush(nums, 2 * curr)
            heapq.heappush(nums, 3 * curr)
            heapq.heappush(nums, 5 * curr)


n = 59
# [_ for _ in solve(n)]
print(list(solve(n)))
