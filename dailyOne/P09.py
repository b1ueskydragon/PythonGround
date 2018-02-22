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


# a = [1, 2, 3]
# print(max(a[1:]))
# print(a[0] + max(a[2:]))


# dynamic programming to store: O(N) : Have some problems
def use_cache(nums):
    cache = [nums[0], nums[1]]  # first two elements
    for i, num in enumerate(nums, 2):  # index i start as [2], num start as num[0]
        cache.append(i)
        x = cache[i - 2] + num
        y = cache[i - 1]
        cache[i] = (max(x, y))  # example: num[0] + num[2] vs num[1]
    return cache[-1] - nums[1]


sample = [0, 2, 3, 4, 5, 6]
sampleB = [1, 8, 1, 5, 2, 4, 8, 7, 9]
print(largest_non_adjacent(sample))
print(use_cache(sample))

print(largest_non_adjacent(sampleB))
print(use_cache(sampleB))


# simply one
def incl_excl(nums):
    include_previous_el = 0  # init
    exclude_previous_el = 0  # init
    for num in nums:
        include_current_el = num + exclude_previous_el
        exclude_current_el = max(include_previous_el, exclude_previous_el)

        include_previous_el = include_current_el
        exclude_previous_el = exclude_current_el

    return max(include_current_el, exclude_current_el)


print(incl_excl(sample))
print(incl_excl(sampleB))
