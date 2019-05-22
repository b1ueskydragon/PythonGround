def maximum_sum_of_non_adjacent_elements(nums):
    incl, excl = 0, 0  # include current num or not
    cache_in, cache_ex = 0, 0  # cache that include previous adjacent num or not

    for curr in nums:
        incl = cache_ex + curr
        excl = max(cache_in, cache_ex)  # since both are not adjacent elements of next curr

        cache_in = incl
        cache_ex = excl

    return max(incl, excl)


def maximum_sum_of_non_adjacent_elements_r(nums):
    # cache that include previous adjacent num or not
    incl, excl = 0, 0

    for curr in nums:
        # since both are not adjacent elements of next curr
        new_excl = max(incl, excl)

        # prepare to next curr
        incl = excl + curr
        excl = new_excl

    return max(incl, excl)
