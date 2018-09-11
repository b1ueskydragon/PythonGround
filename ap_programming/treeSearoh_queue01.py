"""
BFS
"""
from queue import Queue


def treeSearoh(given, target):
    """
    O(2^n)
    """
    queue = Queue()
    i = 0
    curr_sum = 0  # sum til current
    res_sum = curr_sum  # candidate
    size = len(given)

    queue.put(curr_sum)
    while not queue.empty():
        curr_sum = queue.get()

        # variables for debug
        res_error = abs(target - res_sum)
        curr_error = abs(target - curr_sum)

        if res_error > curr_error:
            res_sum = curr_sum
        elif curr_sum < target and i < size:
            queue.put(res_sum + given[i])
            queue.put(res_sum)
            i += 1

    return max(curr_sum, res_sum)


# TODO sort desc
nums, x = list(reversed(sorted([10, 34, 55, 77]))), 100  # [10, 34, 55]
print(treeSearoh(nums, x))
