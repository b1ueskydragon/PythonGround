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
