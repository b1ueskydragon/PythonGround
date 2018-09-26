def find_min(nums):
    size = len(nums)
    pivot = size // 2
    lhc = 0
    rhc = pivot

    # candidate
    res = nums[lhc]

    # left half
    for i, num in enumerate(nums, start=1):
        if num > nums[i]:
            print(num, nums[i])
            break

    # right half


given = [_ for _ in range(100, 200)] + [_ for _ in range(50, 100)]

print(find_min(given))
# print(min(given))
