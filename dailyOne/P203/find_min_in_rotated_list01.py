def find_min(nums):
    """
    O(log N)
    Another edition.
    Move only a cursor (Not split given nums)
    """

    def binary_search(num, low, high):
        if low == high:
            return num[low]  # exit case

        pivot = (low + high) // 2
        if nums[pivot] > nums[high]:
            low = pivot + 1
        else:
            high = pivot

        return binary_search(nums, low, high)

    return binary_search(nums, 0, len(nums) - 1)


given = [_ for _ in range(1000, 2000000)] + [_ for _ in range(400, 402)] + [_ for _ in range(500, 900)]
print(find_min(given))
given = [_ for _ in range(50, 200)]
print(find_min(given))
