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
    """
    to_set = set(nums)  # to find in O(1)
    cache = {}
    cnt = 1  # include current num
    for num in nums:
        if cache.get(num) is 'visited':
            cnt += 1

        else:
            if num in to_set:
                if num + 1 in to_set:
                    cache[num + 1] = 'visited'
                if num - 1 in to_set:
                    cache[num - 1] = 'visited'

                cache[num] = 'visited'
                cnt = 1  # reset

    return cnt


given = [103, 104, 106, 4, 5, 7, 8, 9, 100, 2, 3, 101, 102]
print(count_length(given))
