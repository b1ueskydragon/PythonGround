from queue import Queue

"""
With Queue (BFS)

e.g.)
    [curr=1, 34, 55, 99, 77]
    i [curr=(1 + 34), 55, 99, 77]
    e [curr=1, 55, 99, 77]
    ...
"""


def find_x(nums, x, cache=0):
    queue = Queue()
    queue.put(nums[0])
    for i, _ in enumerate(nums, start=1):
        while not queue.empty():
            excl = queue.get()
            incl = excl + nums[i]
            queue.put(compare(x, incl, excl))

            cache = compare(x, cache, queue.get())

    return cache


compare = lambda x, a, b: b if abs(x - a) > abs(x - b) else a

given, target = [3, 5, 7, 9, 11], 18
print(find_x(given, target))
