"""
With recursion (DFS)

e.g.)
    [curr=1, 34, 55, 99, 77]
    i [curr=(1 + 34), 55, 99, 77]
    e [curr=1, 55, 99, 77]
    ...
"""


# TODO (後回し) 枝切り, refactor
# 遠く離れているのは選びづらくなっているので
# e.g) 1 を選び続ける
# そもそもの abs 比較ロジック修正


def find_x(nums, x):
    incl_cache, excl_cache = 0, 0
    for num in nums:
        incl = num + excl_cache
        excl = compare(x, incl_cache, excl_cache)

        incl_cache = incl
        excl_cache = excl

    return compare(x, incl, excl)


def compare(x, a, b):
    if abs(x - a) > abs(x - b):
        return b
    else:
        return a


given = [10, 34, 55, 77]
target = 100
print(find_x(given, target))
