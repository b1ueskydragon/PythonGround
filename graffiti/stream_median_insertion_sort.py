"""
An algorithm that allows a number to be added
and yet keeps the entire list sorted .. insertion sort.

Find (using a binary search)
and insert the incoming number to the right place.
"""


class Solution:
    def __init__(self):
        self.sorted = []

    @staticmethod
    def get_pos(xs, low, high, value):
        while low < high:
            distance = high - low
            mid = high - (distance // 2)
            if distance == 1:
                # print(low, high)
                return high if value >= xs[low] else low
            if value > xs[mid]:
                low = mid + 1
            else:
                high = mid

        return high  # cursors already got crossed; value is the largest one

    def insert(self, num):
        if not self.sorted:
            self.sorted.append(num)  # append to the end
        else:
            index = Solution.get_pos(self.sorted, 0, len(self.sorted), num)
            self.sorted.insert(index, num)

    def get_median(self):
        n = len(self.sorted)
        m = n // 2
        if n % 2 == 0:
            return (self.sorted[m - 1] + self.sorted[m]) / 2.
        else:
            return self.sorted[m]


if __name__ == '__main__':
    a = Solution()
    a.insert(3)
    a.insert(1)
    a.insert(4)
    a.insert(2)

    print(a.sorted)

    xs = [1, 3, 4, 5]
    index = Solution.get_pos(xs, 0, len(xs), 2)
    print(index)

    xs = [1, 3]
    index = Solution.get_pos(xs, 0, len(xs), 4)
    print(index)

    xs = [1, 3, 4, 5]
    index = Solution.get_pos(xs, 0, len(xs), 3)
    print(index)

    xs = [1, 2, 3, 4]
    index = Solution.get_pos(xs, 0, len(xs), 5)
    print(index)

    xs = [1, 2, 3, 4, 5, 6, 8]
    index = Solution.get_pos(xs, 0, len(xs), 7)
    print(index)

    xs = [1]
    index = Solution.get_pos(xs, 0, len(xs), 0)
    print(index)
