"""
An algorithm that allows a number to be added
and yet keeps the entire list sorted .. insertion sort.

Find (using a binary search)
and insert the incoming number to the right place.
"""


class Solution:
    def __init__(self):
        self.res = []

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
        if not self.res:
            self.res.append(num)  # append to the end
        else:
            index = self.get_pos(self.res, 0, len(self.res), num)
            self.res.insert(index, num)

    def get_median(self):
        n = len(self.res)
        m = n // 2
        if n & 1:
            return self.res[m]
        else:
            return (self.res[m - 1] + self.res[m]) / 2.
