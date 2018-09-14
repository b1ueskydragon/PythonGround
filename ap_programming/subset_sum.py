"""
With recursion (DFS)

e.g.)
    [curr=1, 34, 55, 99, 77]
    i [curr=(1 + 34), 55, 99, 77]
    e [curr=1, 55, 99, 77]
    ...
"""


def find_x(nums, x, i=0, cache=0):
    if i == len(nums):
        return cache

    incl = find_x(nums, x, i + 1, cache + nums[i])
    excl = find_x(nums, x, i + 1, cache)

    return compare(x, incl, excl)


def compare(x, a, b):
    if abs(x - a) > abs(x - b):
        return b
    else:
        return a


given, target = [1, 34, 55, 99, 77], 134
print(find_x(given, target))
