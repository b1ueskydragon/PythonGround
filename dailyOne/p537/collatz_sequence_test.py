import unittest

from .solve import collatzSeq, longest_seq


# Also see: https://oeis.org
class CollatzSequenceTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual([1], list(collatzSeq(1)))

    def test_2(self):
        self.assertEqual([2, 1], list(collatzSeq(2)))

    def test_3(self):
        self.assertEqual([3, 10, 5, 16, 8, 4, 2, 1], list(collatzSeq(3)))

    def test_4(self):
        self.assertEqual([4, 2, 1], list(collatzSeq(4)))

    def test_5(self):
        self.assertEqual([5, 16, 8, 4, 2, 1], list(collatzSeq(5)))

    def test_6(self):
        self.assertEqual([6, 3, 10, 5, 16, 8, 4, 2, 1], list(collatzSeq(6)))

    def test_7(self):
        self.assertEqual([7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], list(collatzSeq(7)))

    def test_8(self):
        self.assertEqual([8, 4, 2, 1], list(collatzSeq(8)))

    def test_9(self):
        self.assertEqual([9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], list(collatzSeq(9)))

    def test_10(self):
        self.assertEqual([10, 5, 16, 8, 4, 2, 1], list(collatzSeq(10)))

    def test_14(self):
        self.assertEqual([14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], list(collatzSeq(14)))

    def test_15(self):
        self.assertEqual([15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1], list(collatzSeq(15)))

    # def test_longest_seq(self):
    #     self.assertEqual([1, 1, 2, 8, 3, 6, 9, 17, 4, 20, 7], longest_seq(10))
