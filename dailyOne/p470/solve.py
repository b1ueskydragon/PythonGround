"""
The nearest large number of the number at index i.

if two distances to larger numbers are the equal, then return any one of them.
if the array at i doesn't have a nearest larger integer, then return null.
"""


def theNearestLargeNumber(nums, i):
    # binary search
    N = len(nums)
    num = nums[i]
    l, r = i - 1, i + 1
    while l > -1 or r < N:
        if l > -1:
            if nums[l] > num:
                return l
            else:
                l -= 1
        if r < N:
            if nums[r] > num:
                return r
            else:
                r += 1
    return None
