import unittest

from graffiti.stream_median import Solution as A


class StreamMedianTest(unittest.TestCase):
    @staticmethod
    def test_only_for_debug_inner_structure():
        a = A()
        integer_stream = [31, 22, 45, -9, 10, 0, 78, 9]
        for v in integer_stream:
            a.insert(v)
        print('left', a._left_heap)
        print('right', a._right_heap)

    def test_odd_len_stream_returns_a_pivot(self):
        a = A()
        nums = [3, 4, 2, 1, 5]
        for v in nums:
            a.insert(v)
        self.assertEqual(3, a.get_median())

    def test_even_len_stream_returns_average_of_two_pivots(self):
        a = A()
        nums = [3, -4, 2, -1, 5]
        for v in nums:
            a.insert(v)
        a.insert(6)
        self.assertEqual(2.5, a.get_median())
