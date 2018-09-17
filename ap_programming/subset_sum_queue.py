from queue import Queue

"""
With Queue (BFS)

e.g.)
    [curr=1, 34, 55, 99, 77]
    i [curr=(1 + 34), 55, 99, 77]
    e [curr=1, 55, 99, 77]
    ...
"""


def find_x(nums, x, i=0, cache=0):
    queue = Queue()
    incl, excl = 0, 0

    while not queue.empty():
        excl = queue.get()
        incl = excl + nums[i]

        for num in nums:
            queue.put(excl)
            queue.put(incl)

    return compare(x, incl, excl)


compare = lambda x, a, b: b if abs(x - a) > abs(x - b) else a

given, target = [1, 34, 55, 99, 77], 134
print(find_x(given, target))
