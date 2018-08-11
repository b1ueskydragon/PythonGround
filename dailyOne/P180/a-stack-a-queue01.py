from queue import Queue
import math


def interleave_half(stack):
    """
    -1th
    S [3,2,1]
    Q (5,4)

    S [1,5,2,4,3]
    """
    qu = Queue()
    size = len(stack)

    while stack:
        qu.put(stack.pop())

    for _ in range(int(size / 2)):
        qu.put(qu.get())

    return stack


given_odd = [1, 2, 3, 4, 5]
given_even = [1, 2, 3, 4]

print(interleave_half(given_odd))
