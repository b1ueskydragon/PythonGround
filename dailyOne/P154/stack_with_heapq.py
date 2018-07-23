from time import time
import heapq


class Stack:
    def __init__(self):
        pass


# TODO Rename `Heap`: make more specific
class Heap:
    """
    Impl a `Heap` with making value a pair (Tuple).
    """
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        """
        adds a new key to the heap.

        :param item:
        :param priority:
        """
        heapq.heappush(self.heap, (-priority, item))  # Tuple

    def pop(self):
        """
        removes and returns the max value of the heap.

        :return:
        """
        _, item = heapq.heappop(self.heap)  # Tuple
        return item


# Test
heap = Heap()
heap.push('c', 0)
print(heap.heap)  # [(0, 'c')]
heap.push('a', 1)
print(heap.heap)  # [(-1, 'a'), (0, 'c')]
heap.push('b', 2)
print(heap.heap)  # [(-2, 'b'), (0, 'c'), (-1, 'a')]
print(heap.pop())  # b
print(heap.heap)  # [(-1, 'a'), (0, 'c')]
