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
    # an example of the integer stream in range [1, 10], and the number comes randomly.
    a.min_heap = [1, 2, 3, 4, 5]
    a.max_heap = [-10, -9, -8, -7, -6]
    res = a.get_median()
    print(res)
