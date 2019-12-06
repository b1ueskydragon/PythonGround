import unittest

from dailyOne.p379.solve import subsequence


class KmpTest(unittest.TestCase):
    def test_xyz(self):
        """
        Note that zx is not a valid subsequence.
        Since it is not in the order of the given string.
        """
        string = "xyz"
        expected = ["", "x", "y", "xy", "z", "xz", "yz", "xyz"]

        self.assertEqual(expected, subsequence(string))
