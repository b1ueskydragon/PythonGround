import unittest

from graffiti.stream_median_insertion_sort import Solution as B


class StreamMedianTest(unittest.TestCase):
    def test_is_sorted(self):
        b = B()
        integer_stream = [31, 22, 45, -9, 10, 0, 78, 9]
        for v in integer_stream:
            b.insert(v)
        self.assertEqual(list(sorted(integer_stream)), b.res)

    def test_get_a_right_pos(self):
        b = B()
        b.insert(3)
        b.insert(1)
        b.insert(4)
        b.insert(2)

        xs = [1, 3, 4, 5]
        index = B().get_pos(xs, 0, len(xs), 2)
        self.assertEqual(1, index)

        xs = [1, 3]
        index = B().get_pos(xs, 0, len(xs), 4)
        self.assertEqual(2, index)

        xs = [1, 3, 4, 5]
        index = B().get_pos(xs, 0, len(xs), 3)
        self.assertEqual(1, index)

        xs = [1, 2, 3, 4]
        index = B().get_pos(xs, 0, len(xs), 5)
        self.assertEqual(4, index)

        xs = [1, 2, 3, 4, 5, 6, 8]
        index = B().get_pos(xs, 0, len(xs), 7)
        self.assertEqual(6, index)

        xs = [1]
        index = B().get_pos(xs, 0, len(xs), 0)
        self.assertEqual(0, index)

    def test_odd_len_stream_returns_a_pivot(self):
        b = B()
        nums = [3, 4, 2, 1, 5]
        for v in nums:
            b.insert(v)
        self.assertEqual(3, b.get_median())

    def test_even_len_stream_returns_average_of_two_pivots(self):
        b = B()
        nums = [3, -4, 2, -1, 5]
        for v in nums:
            b.insert(v)
        b.insert(6)
        self.assertEqual(2.5, b.get_median())
