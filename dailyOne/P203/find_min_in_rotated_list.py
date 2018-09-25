def find_min(nums):
    # O(log N) -> half, half, half ...
    # half-division logic ?

    # find max at first

    pivot = len(nums) // 2

    lh = min(nums[:pivot])
    rh = min(nums[pivot:])

    # ↑ min, max is O(N)

    return min(lh, rh)


given = [2, 3, 4, 5, 1]
print(find_min(given))  # 1

# given = [5, 7, 10, 3, 4]
# print(find_min(given))  # 3
# given = [5, 7, 3, 4]
# print(find_min(given))  # 3
# given = [4, 5, 1, 2, 3]
# print(find_min(given))  # 1
