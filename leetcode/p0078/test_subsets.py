import unittest
from leetcode.p0078.solve import Solution as A


class SubSetsCase(unittest.TestCase):
    def test_all_distinct(self):
        a = A()
        nums = [1, 2, 3]
        expected = [
            [3],
            [1],
            [2],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ]
        self.assertEqual(expected, a.subsets(nums))

    def test_has_duplication(self):
        a = A()
        nums = [1, 2, 2]
        expected = [
            [2],
            [1],
            [1, 2, 2],
            [1, 2],
            [2, 2],
            []
        ]
        self.assertEqual(expected, a.subsets(nums))


if __name__ == '__main__':
    unittest.main()
