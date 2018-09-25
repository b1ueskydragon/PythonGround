def find_min(nums):
    size = len(nums)
    head = nums[0]
    last = nums[size - 1]
    pivot = size // 2  # TODO pivot ?

    if head < last:
        nums = nums[:pivot]
    else:
        nums = nums[pivot:]

    if size <= 1:
        return head
    else:
        return find_min(nums)

    # TODO find `max`


# given = [2, 3, 4, 5, 1]
# print(find_min(given) == min(given))  # 1
# given = [3, 4, 5, 6, 1, 2]
# print(find_min(given) == min(given))  # 1
# given = [0, 2, 4, 6, 8, 10]
# print(find_min(given) == min(given))  # 0
# given = [5, 7, 10, 3, 4]
# print(find_min(given) == min(given))  # 3
# given = [5, 7, 3, 4]
# print(find_min(given) == min(given))  # 3
# given = [4, 5, 1, 2, 3]
# print(find_min(given) == min(given))  # 1

# TODO
given = [_ for _ in range(100, 200)] + [_ for _ in range(50, 100)]
print(find_min(given) == min(given))  # 50
