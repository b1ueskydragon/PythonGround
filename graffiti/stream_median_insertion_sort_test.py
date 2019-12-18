import unittest

from graffiti.stream_median_insertion_sort import Solution as B


class StreamMedianTest(unittest.TestCase):
    @staticmethod
    def test_only_for_debug_inner_structure():
        b = B()
        integer_stream = [31, 22, 45, -9, 10, 0, 78, 9]
        for v in integer_stream:
            b.insert(v)
        print('sorted list', b.sorted)

    def test_get_pos(self):
        pass

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
