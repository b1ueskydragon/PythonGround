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


def count_length(nums):
    """
    O(N)

    Using bound, update bound in-place.

    mapping {current num : (left bound so far, right bound so far)}
    """
    cache = {}  # find key in O(1)
    size = 0  # current max
    for num in nums:
        if num in cache:
            continue

        left = num
        right = num

        if num - 1 in cache:  # 今まで見てきたなかで. so far.
            left = cache[num - 1][0]
        if num + 1 in cache:
            right = cache[num + 1][1]

        cache[num] = (left, right)
        cache[left] = (left, right)
        cache[right] = (left, right)

        size = max(right - left + 1, size)

    return size


given = [103, 104, 104, 106, 4, 5, 7, 8, 9, 100, 2, 3, 101, 102]
print(count_length(given))

given01 = [100, 4, 200, 1, 3, 2]
print(count_length(given01))
