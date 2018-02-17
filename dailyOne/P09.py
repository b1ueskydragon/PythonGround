import math


def large_sum_non_adjacent(nums):  # WIP : if len(nums) == 4
    if len(nums) == 0:
        return 0

    buff_list = []

    center = math.ceil(len(nums) / 2)

    left_half = nums[:center]
    if len(left_half) == 2:  # left half
        if left_half[0] > left_half[1]:
            buff_list.append(left_half[0])
        else:
            buff_list.append(left_half[1])

    right_half = nums[center:]
    if len(right_half) == 2:  # right half
        if right_half[0] > right_half[1]:
            buff_list.append(right_half[0])
        else:
            buff_list.append(right_half[1])

    return buff_list  # WIP: リストを絞っていく (recursion)


print(large_sum_non_adjacent([2, 4, 6, 8]))  # 12
print(large_sum_non_adjacent([5, 1, 1, 5]))  # 10

# 総当たり O(n(n-1)/2) == O(n^2)
# O(n) ?
