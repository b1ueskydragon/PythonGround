"""
@b1ueskydragon
"""

import math


# リストを絞っていく
def large_sum_non_adjacent(nums):
    if len(nums) <= 2:
        return max(nums)

    buff = []
    center = math.ceil(len(nums) / 2)

    left_half = nums[:center]  # left half
    find_helper(left_half, buff)

    right_half = nums[center:]  # right half
    find_helper(right_half, buff)

    return buff


def find_helper(nums, buff):
    if len(nums) <= 2:
        buff.append(max(nums))
    else:
        find_helper(nums[2:], buff)


#print(large_sum_non_adjacent([2, 4, 6, 8]))  # 12
#print(large_sum_non_adjacent([5, 1, 1, 5]))  # 10
#print(large_sum_non_adjacent([5, 1, 1, 5, 2, 4, 8, 7]))  # 5, 8

print(large_sum_non_adjacent([1, 8, 1, 5, 2, 4, 8, 7]))  # 8, 8


# print(large_sum_non_adjacent([5, 1, 1, 5, 2, 4, 6, 8, 11]))  # .. ?

# 総当たり O(n(n-1)/2) == O(n^2)
# O(n) ?
