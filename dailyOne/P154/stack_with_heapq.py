"""
Implement a stack API using ONLY a heap.

most recently := largest
"""

from time import time
import heapq


class Stack:
    def __init__(self):
        self.phq = PriorityHeapq()

    def push(self, item):
        """
        adds an element to the stack.
        :param item:
        """
        self.phq.push(item, time())

    def pop(self):
        """
        removes and returns the most recently added element.
        """
        if not self.phq.heap:
            raise IndexError('nothing on the stack')

        return self.phq.pop()


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
