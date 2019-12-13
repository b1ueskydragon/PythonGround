class Solution:
    def __init__(self):
        # a default heap in min heap
        self.min_heap = []
        # make a heap behave like a max heap by inversion
        self.max_heap = []
        # size of the integer stream
        self.N = 0

    def insert(self, num):
        pass  # TODO

    def get_median(self):
        if self.N % 2 == 0:
            return (-1 * self.max_heap[0] + self.min_heap[0]) / 2.
        else:
            return -1 * self.max_heap[0]


if __name__ == '__main__':
    a = Solution()
