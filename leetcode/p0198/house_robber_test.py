import unittest

from leetcode.p0198.solve import Solution as A


class HouseRobberTest(unittest.TestCase):
    def test_random_big_numbers(self):
        a = A()
        nums = [27745, 27518, 54612, 79175, 55310,
                38265, 73079, 42208, 37513, 18112,
                73627, 91755, 60797, 78407, 29146,
                11707, 42650, 12111, 36290, 82890,
                60637, 51963, 83323, 78120, 61634,
                12828, 36784, 53898, 50094, 83697,
                89871, 28950, 69294, 69762, 65189,
                83559, 68085, 41715, 88143, 27856,
                9949, 2575, 6319, 78964, 43587,
                14981, 84885, 84898, 2467, 95751]
        self.assertEqual(1454958, a.rob(nums))

    def test_example_1(self):
        a = A()
        nums = [1, 2, 3, 1]  # 1 + 3
        self.assertEqual(4, a.rob(nums))

    def test_example_2(self):
        a = A()
        nums = [2, 7, 9, 3, 1]  # 2 + 9 + 1
        self.assertEqual(12, a.rob(nums))

    def test_only_one_num(self):
        a = A()
        nums = [99]
        self.assertEqual(99, a.rob(nums))

    def test_empty_list(self):
        a = A()
        nums = []
        self.assertEqual(0, a.rob(nums))
