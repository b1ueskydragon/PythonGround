import unittest

from leetcode.p0504.solve import Solution as A


class ConvertToBase7Test(unittest.TestCase):
    def test_boundary_maximum(self):
        a = A()
        self.assertEqual("150666343", a.convertToBase7(int(1e7)))

    def test_boundary_minimum(self):
        a = A()
        self.assertEqual("-150666343", a.convertToBase7(int(-1e7)))

    def test_zero(self):
        a = A()
        self.assertEqual("0", a.convertToBase7(0))

    def test_stack_all_digits(self):
        a = A()
        self.assertEqual("150666342", a.convertToBase7(9999999))
