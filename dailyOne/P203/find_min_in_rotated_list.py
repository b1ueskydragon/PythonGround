def find_min(nums):
    """
    Do it O(log N) time
     - Use binary search
    """
    size = len(nums)
    pivot = size // 2
    head = 0
    last = size - 1

    if size == 2:
        return min(nums)
    elif nums[pivot] > nums[last]:
        return find_min(nums[pivot:size])
    else:
        return find_min(nums[head:pivot + 1])


# TODO set more bigger range ...
given = [_ for _ in range(1000, 2000)] + [_ for _ in range(400, 402)] + [_ for _ in range(500, 900)]
print(find_min(given))
given = [_ for _ in range(50, 200)]
print(find_min(given))
