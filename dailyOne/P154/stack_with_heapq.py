from time import time
import heapq


class Stack:
    def __init__(self):
        pass


class PriorityHeapq:
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
phq = PriorityHeapq()
phq.push('c', 0)
print(phq.heap)  # [(0, 'c')]
phq.push('a', 1)
print(phq.heap)  # [(-1, 'a'), (0, 'c')]
phq.push('b', 2)
print(phq.heap)  # [(-2, 'b'), (0, 'c'), (-1, 'a')]
print(phq.pop())  # b
print(phq.heap)  # [(-1, 'a'), (0, 'c')]
