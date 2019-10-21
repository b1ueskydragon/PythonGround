import unittest
from heapq import heappop

from retrospective import find_multiple_max


class FindMultipleMaxTest(unittest.TestCase):
    def test_standard(self):
        xs = [-3, 98, -99, 97]
        self.assertEqual(-28518, find_multiple_max.solve(xs))

    def test_size_is_less_than_three(self):
        xs = [99, 97]
        self.assertEqual(-1, find_multiple_max.solve(xs))

    def test_reversed_heapify(self):
        xs = [-3, 98, -99, 97]
        actual = find_multiple_max.reversed_heapify(xs)
        self.assertEqual(98, heappop(actual) * -1)
        self.assertEqual(97, heappop(actual) * -1)
        self.assertEqual(-3, heappop(actual) * -1)
        self.assertEqual(-99, heappop(actual) * -1)


if __name__ == '__main__':
    unittest.main()
