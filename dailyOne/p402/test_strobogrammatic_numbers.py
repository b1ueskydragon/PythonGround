import unittest

from dailyOne.p402.solve import strobogrammatic_numbers


class StrobogrammaticNumbersTest(unittest.TestCase):
    def test_digit_1(self):
        expected = [0, 1, 8]
        self.assertEqual(expected, strobogrammatic_numbers(1))

    def test_digit_2(self):
        expected = [11, 69, 88, 96]
        self.assertEqual(expected, strobogrammatic_numbers(2))

    def test_digit_3(self):
        expected = [101, 111, 181,
                    609, 619, 689,
                    808, 818, 888,
                    906, 916, 986]
        self.assertEqual(expected, strobogrammatic_numbers(3))

    def test_digit_4(self):
        expected = [1001, 1111, 1691, 1881, 1961,
                    6009, 6119, 6699, 6889, 6969,
                    8008, 8118, 8698, 8888, 8968,
                    9006, 9116, 9696, 9886, 9966]
        self.assertEqual(expected, strobogrammatic_numbers(4))


if __name__ == '__main__':
    unittest.main()
