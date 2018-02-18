# straightforward: O(2^N)
def largest_non_adjacent(arr):
    if len(arr) <= 2:
        return max(arr)
    a = largest_non_adjacent(arr[1:])
    head = arr[0]
    b = head + largest_non_adjacent(arr[2:])
    return max(a, b)


# print(largest_non_adjacent([1, 8, 1, 5, 2, 4, 8, 7]))  # 8, 5, 4, 7
# print(largest_non_adjacent([1, 8, 1, 5, 2, 4, 8, 7, 9]))  # 8, 5, 8, 9


a = [1, 2, 3]
print(max(a[1:]))
print(a[0] + max(a[2:]))


# dynamic programming to store: O(N) : Have some problems
def use_cache(nums):
    cache = [nums[0], nums[1]]  # first two elements
    for i, num in enumerate(nums, 2):  # index i start as [2], num start as num[0]
        cache.append(i)
        x = cache[i - 2] + num
        y = cache[i - 1]
        cache[i] = (max(x, y))  # example: num[0] + num[2] vs num[1]
    return cache[-1]


print(use_cache([0, 2, 3, 4, 5, 6]))
