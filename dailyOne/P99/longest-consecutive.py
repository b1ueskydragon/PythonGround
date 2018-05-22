"""
find the length of the longest consecutive elements sequence in O(n).
"""


def count_length_sorted(nums):
    """
    O(N logN)
    """
    nums = sorted(nums)
    cnt, tmp = 1, 0

    for i, v in enumerate(nums, 1):
        if i is len(nums):
            break
        if nums[i] - v == 1:
            cnt += 1
        else:
            tmp = max(cnt, tmp)
            cnt = 1  # reset

    return max(cnt, tmp)


given = [103, 104, 106, 4, 5, 7, 8, 9, 100, 2, 3, 101, 102]  # 5
print(count_length_sorted(given))
