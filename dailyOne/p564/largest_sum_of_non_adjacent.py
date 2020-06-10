"""
Numbers can be 0 or negative.
"""
import math


def largest_sum_of_non_adjacent(nums):
    res = incl_curr = excl_curr = -math.inf

    for num in nums:
        incl_curr_bef = incl_curr
        incl_curr = max(num, num + excl_curr)
        excl_curr = max(incl_curr_bef, excl_curr)
        res = max(excl_curr, incl_curr, res)
    return res
