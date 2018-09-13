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


def find_x(nums, x, cache):
    res = nums[0]
    incl_next = res + nums[1]
    excl_next = res

    find_x(nums, x, incl_next)
    find_x(nums, x, excl_next)

    return res


given, target = [1, 3, 5, 7, 9], 10
print(find_x(given, target, 0))
