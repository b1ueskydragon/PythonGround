import heapq
import random


def heapsort(iterable, h=[]):
    # pushing all values onto a heap
    for value in iterable:
        heapq.heappush(h, value)
    # then popping off the smallest values one at a time
    return [heapq.heappop(h) for _ in range(len(h))]


it = list(range(10))
random.shuffle(it)
print(it)
print(heapsort(it))
