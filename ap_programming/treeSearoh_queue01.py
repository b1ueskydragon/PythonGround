"""
BFS
"""
from queue import Queue


def treeSearoh(given, target):
    queue = Queue()
    i = 0
    curr_sum = given[i]  # sum til current
    res_sum = curr_sum  # candidate
    last = len(given) - 1

    queue.put(curr_sum)
    while not queue.empty():
        curr_sum = queue.get()
        if abs(target - res_sum) > abs(target - curr_sum):
            res_sum = curr_sum
        elif curr_sum < target and i is not last:
            i += 1  # TODO 一周しかしない (2^n 探索必要)
            queue.put(curr_sum + given[i])
            queue.put(curr_sum)

    return max(curr_sum, res_sum)


# TODO sort desc
nums, x = list(reversed(sorted([10, 34, 55, 77]))), 100  # [10, 34, 55]
print(treeSearoh(nums, x))
