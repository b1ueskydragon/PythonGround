def find_use_set(nums):
    to_set = set(nums)  # O(1)
    i = 1
    while i in to_set:
        i += 1
    return i


given = [-2, 10, 5, 3, 2]
print(find_use_set(given))
