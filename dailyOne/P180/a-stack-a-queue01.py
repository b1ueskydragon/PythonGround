from queue import Queue
import math


def interleave_half(stack):
    """
    -1th
    S [3,2,1]
    Q (5,4)

    Q (1,5,2,4,3)
    S [1,5,2,4,3]
    """
    qu = Queue()
    size = len(stack)

    pivot = size // 2
    move = int(math.ceil(size / 2))  # `pivot + 1` if is odd

    while stack:
        qu.put(stack.pop())

    for _ in range(pivot):
        qu.put(qu.get())

    for _ in range(move):
        stack.append(qu.get())

    for _ in range(pivot):
        qu.put(stack.pop())
        qu.put(qu.get())

    if stack:
        qu.put(stack.pop())

    while not qu.empty():
        stack.append(qu.get())

    return stack


given_odd = [1, 2, 3, 4, 5]
given_even = [1, 2, 3, 4]

print(interleave_half(given_odd))
print(interleave_half(given_even))
