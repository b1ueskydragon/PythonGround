"""
With recursion (DFS)

e.g.)
    [curr=1, 34, 55, 99, 77]
    i [curr=(1 + 34), 55, 99, 77]
    e [curr=1, 55, 99, 77]
    ...
"""


# TODO (後回し) 枝切り, refactor


def find_x(nums, x, cache):
    res = nums[0]
    incl_next = res + nums[1]
    excl_next = res

    incl_err = abs(x - incl_next)
    excl_err = abs(x - excl_next)
    if incl_err > excl_err:
        res = excl_next
    else:
        res = incl_next
    for i in range(1, len(nums) - 1):
        cache_err = abs(x - cache)
        curr_err = abs(x - res)
        if cache_err > curr_err:
            cache = res
        return find_x(nums[i:], x, cache)

    return cache


given, target = [1, 3, 5, 7, 9], 10
print(find_x(given, target, 0))
