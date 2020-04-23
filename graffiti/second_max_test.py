import random
import unittest

from graffiti.second_max import second_max


class SecondMaxTest(unittest.TestCase):
    def test_sample(self):
        xs = [10, 20, 4, 45, 99]
        self.assertEqual(second_max(xs), list(sorted(xs, reverse=True))[1])

    def test_all_equivalent(self):
        xs = [1] * 100
        self.assertEqual(second_max(xs), list(sorted(xs, reverse=True))[1])

    def test_big_numbers(self):
        xs = [27745, 27518, 54612, 79175, 55310,
              38265, 73079, 42208, 37513, 18112,
              73627, 91755, 60797, 78407, 29146,
              11707, 42650, 12111, 36290, 82890,
              60637, 51963, 83323, 78120, 61634,
              12828, 36784, 53898, 50094, 83697,
              89871, 28950, 69294, 69762, 65189,
              83559, 68085, 41715, 88143, 27856,
              9949, 2575, 6319, 78964, 43587,
              14981, 84885, 84898, 2467, 95751]
        self.assertEqual(second_max(xs), list(sorted(xs, reverse=True))[1])

    def test_random_list(self):
        xs = random.sample(range(0, 10000), k=1000)
        self.assertEqual(second_max(xs), list(sorted(xs, reverse=True))[1])
