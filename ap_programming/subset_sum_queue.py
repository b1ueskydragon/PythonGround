from queue import Queue

"""
With Queue (BFS)

e.g.)
    [curr=1, 34, 55, 99, 77]
    i [curr=(1 + 34), 55, 99, 77]
    e [curr=1, 55, 99, 77]
    ...
"""


def find_x(nums, x, i=1, cache=0):
    queue = Queue()
    queue.put(nums[0])

    while not queue.empty():
        curr = queue.get()
        cache = compare(x, cache, curr)

        if i < len(nums):
            excl = nums[i]
            incl = excl + nums[i]
            queue.put(excl)
            queue.put(incl)
            i += 1

    return cache


compare = lambda x, a, b: b if abs(x - a) > abs(x - b) else a

given, target = [3, 5, 7, 9, 11], 16
print(find_x(given, target))
