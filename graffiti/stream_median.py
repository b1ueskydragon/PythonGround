"""
a median is the middle element in an odd length sorted array,
and in the even case it’s the average of the middle elements
"""
import heapq


class Solution:
    def __init__(self):
        # a default heap (min heap)
        self._right_heap = []
        # make a heap behave like a max heap by inversion
        self._left_heap = []
        # we don't know the length of `stream`, so an init is 0 and increase it.
        self._N = 0

    def insert(self, num):
        heapq.heappush(self._left_heap, -1 * num)
        if self._N % 2 == 0:
            if not self._right_heap:
                self._N += 1  # count-up only
                return
            if -1 * self._left_heap[0] > self._right_heap[0]:  # swap
                min_val = heapq.heappop(self._left_heap)
                max_val = heapq.heappop(self._right_heap)
                heapq.heappush(self._right_heap, -1 * min_val)
                heapq.heappush(self._left_heap, -1 * max_val)
        else:
            min_val = heapq.heappop(self._left_heap)
            heapq.heappush(self._right_heap, -1 * min_val)
        self._N += 1

    def get_median(self):
        l_max = -1 * self._left_heap[0]
        if self._N % 2 == 0:  # two pivots
            r_min = self._right_heap[0]
            return (l_max + r_min) / 2.
        else:
            return l_max
