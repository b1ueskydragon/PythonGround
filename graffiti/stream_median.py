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
            self._N += 1
            if not self._right_heap:
                return
            if -1 * self._left_heap[0] > self._right_heap[0]:
                min_val = -1 * heapq.heappop(self._left_heap)
                max_val = heapq.heappop(self._right_heap)

                heapq.heappush(self._right_heap, min_val)
                heapq.heappush(self._left_heap, -1 * max_val)
        else:
            self._N += 1
            min_val = -1 * heapq.heappop(self._left_heap)
            heapq.heappush(self._right_heap, min_val)

    def get_median(self):
        if self._N % 2 == 0:  # two pivots
            l_max, r_min = -1 * self._left_heap[0], self._right_heap[0]
            print(l_max, r_min)
            return (l_max + r_min) / 2.
        else:
            return -1 * self._left_heap[0]


if __name__ == '__main__':
    # for debugging
    a = Solution()
    integer_stream = [31, 22, 45, -9, 10, 0, 78, 9]
    for v in integer_stream:
        a.insert(v)
    print('left', a._left_heap)
    print('right', a._right_heap)
