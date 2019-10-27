"""
Write a Python program to find unique triplets
whose three elements gives the sum of zero from an array of n integers
"""

import itertools


def find_unique_triplets(nums):
    res = []
    n = len(nums)
    zs = set(nums)
    for i in range(n):
        for j in range(i, n):
            x, y = nums[i], nums[j]
            if x == y:
                continue
            z = -(x + y)
            if x == z or y == z:
                continue
            if z in zs:
                t = sorted((x, y, z))
                if t not in res:
                    res.append(t)
                break
    return res


xs = [3, 5, -7, 11, 2]
print(find_unique_triplets(xs))  # 2, 5, -7

ys = [1, -6, 4, 2, -1, 2, 0, -2, 0]
print(find_unique_triplets(ys))  # -6, 4, 2 or 1, -1, 0 or 2, 0, -2

# use built-in combinations
print(list(filter(lambda t: sum(t) == 0, itertools.combinations(set(xs), 3))))
print(list(filter(lambda t: sum(t) == 0, itertools.combinations(set(ys), 3))))
