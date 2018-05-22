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

    mapping
    {current start point(num) : nums seen so far}
    """
    to_set = set(nums)  # to find in O(1)
    cache = {}
    visited = {}
    cnt = 1  # include current num
    for num in nums:
        if visited.get(num) is 'visited':
            continue
        else:
            cache[num] = {num}
            visited[num] = 'visited'

            if num - 1 in to_set:
                cache.get(num).add(num - 1)
                visited[num - 1] = 'visited'

            if num + 1 in to_set:
                cache.get(num).add(num + 1)
                visited[num + 1] = 'visited'

    return cache


given = [103, 104, 106, 4, 5, 7, 8, 9, 100, 2, 3, 101, 102]
print(count_length(given))
