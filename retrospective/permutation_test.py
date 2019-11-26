import unittest
from math import factorial

from retrospective.permutation import permutation


class PermutationTest(unittest.TestCase):
    def test_3P2(self):
        xs = ['a', 'b', 'c']
        n = len(xs)
        k = 2

        expected = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']
        actual = list(map(''.join, permutation(xs, k)))
        self.assertEqual(expected, actual)

        expected_len = factorial(n) // factorial(n - k)
        self.assertEqual(expected_len, len(actual))

    def test_4P2(self):
        xs = ['a', 'b', 'c', 'd']
        n = len(xs)
        k = 2

        expected = ['ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca', 'cb', 'cd', 'da', 'db', 'dc']
        actual = list(map(''.join, permutation(xs, k)))
        self.assertEqual(expected, actual)

        expected_len = factorial(n) // factorial(n - k)
        self.assertEqual(expected_len, len(actual))

    def test_4P3(self):
        xs = ['a', 'b', 'c', 'd']
        n = len(xs)
        k = 3

        expected = ['abc', 'abd', 'acb', 'acd', 'adb', 'adc',
                    'bac', 'bad', 'bca', 'bcd', 'bda', 'bdc',
                    'cab', 'cad', 'cba', 'cbd', 'cda', 'cdb',
                    'dab', 'dac', 'dba', 'dbc', 'dca', 'dcb']
        actual = list(map(''.join, permutation(xs, k)))
        self.assertEqual(expected, actual)

        expected_len = factorial(n) // factorial(n - k)
        self.assertEqual(expected_len, len(actual))
