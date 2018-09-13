"""
Arranged edition of `treeSearoh`
"""


def find_x(nums, x):
    cache = 0  # candidate of sum result on overall
    for i in range(len(nums)):
        curr = 0  # candidate of sum result in this list
        for num in nums[i:]:
            if num is x:
                return num

            inc_next = curr + num  # select next
            exc_next = curr  # not select next

            # select exc_next vs inc_next
            inc_error = abs(x - inc_next)
            exc_error = abs(x - exc_next)
            if inc_error > exc_error:
                curr = exc_next
            else:
                curr = inc_next

        # select cache vs res_sum
        cache_error = abs(x - cache)
        res_error = abs(x - curr)
        if cache_error > res_error:
            cache = curr

    return cache


given, target = [1, 34, 55, 99, 77], 134  # TODO Fix bug: make pick 1, 34, 99
print(find_x(given, target))
