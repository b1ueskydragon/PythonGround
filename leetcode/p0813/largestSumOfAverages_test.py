import unittest
from leetcode.p0813.solve import Solution


class MyTestCase(unittest.TestCase):
    def test_largestSumOfAverages(self):
        s = Solution()
        A = [9, 1, 2, 3, 9]
        K = 3

        expected = float(20)  # [9] [1,2,3] [9]
        actual = s.largestSumOfAverages(A, K)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
