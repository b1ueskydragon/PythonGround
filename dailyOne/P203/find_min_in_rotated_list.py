def find_min(nums):
    size = len(nums)

    for i, num in enumerate(nums, start=1):
        if i == size:
            return nums[0]
        elif num > nums[i]:
            return nums[i]


given = [_ for _ in range(100, 200)] + [_ for _ in range(50, 100)]
print(find_min(given))
given = [_ for _ in range(50, 200)]
print(find_min(given))
