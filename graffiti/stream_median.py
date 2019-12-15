"""
a median is the middle element in an odd length sorted array,
and in the even case it’s the average of the middle elements
"""
import heapq


class Solution:
    def __init__(self):
        # a default heap in min heap
        self.min_heap = []
        # make a heap behave like a max heap by inversion
        self.max_heap = []
        # we don't know the length of `stream`, so an init is 0 and increase it.
        self.N = 0

    def insert(self, num):
        heapq.heappush(self.max_heap, -1 * num)
        # TODO
        self.N += 1

    def get_median(self):
        if len(self.min_heap) % 2 != 0:
            return -1 * self.max_heap[0], self.min_heap[0]
        else:
            return -1 * self.max_heap[0]


if __name__ == '__main__':
    a = Solution()
    integer_stream = [3, 4, 2, 1, 5]
    a.N = len(integer_stream)
    for v in integer_stream:
        a.insert(v)
    print('min', a.min_heap)
    print('max', a.max_heap)
    print(a.N)
    print(sum(integer_stream) / len(integer_stream))
    print(a.get_median())
