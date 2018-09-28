def find_min(nums):
    """
    Another edition.
    O(log N)
    """
    # TODO call binary_search


def binary_search(arr, low, high):
    if low == high:
        return arr[low]

    pivot = (low + high) // 2
    if arr[pivot] < arr[high]:
        high = pivot
    else:
        low = pivot + 1

    return binary_search(arr, low, high)

# given = [_ for _ in range(1000, 2000)] + [_ for _ in range(400, 402)] + [_ for _ in range(500, 900)]
# print(find_min(given))
# given = [_ for _ in range(50, 200)]
# print(find_min(given))
