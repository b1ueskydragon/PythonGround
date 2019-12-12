import heapq


class Solution:
    def __init__(self):
        # a default heap in min heap
        self.min_heap = []
        # make a heap behave like a max heap by inversion
        self.max_heap = []
        self.N = 0

    def insert(self, num):
        if self.N % 2 == 0:  # TODO ?
            heapq.heappush(self.max_heap, -1 * num)
        else:
            to_min = -1 * heapq.heappushpop(self.max_heap, -1 * num)


if __name__ == '__main__':
    a = Solution()
