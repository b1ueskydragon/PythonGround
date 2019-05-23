def maximum_sum_of_non_adjacent_elements(nums):
    incl, excl = 0, 0
    for curr in nums:
        prev_incl = incl

        incl = curr + excl
        excl = max(prev_incl, excl)

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
