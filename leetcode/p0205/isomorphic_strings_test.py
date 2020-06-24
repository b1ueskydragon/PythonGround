import unittest
from .isomorphic_strings import Solution as A


class IsomorphicStringsTest(unittest.TestCase):
    def test_true(self):
        a = A()
        self.assertTrue(a.isIsomorphic("egg", "add"))
        self.assertTrue(a.isIsomorphic("paper", "title"))
        self.assertTrue(a.isIsomorphic("egggggga", "addddddc"))
        self.assertTrue(a.isIsomorphic("", ""))
        self.assertTrue(a.isIsomorphic("x", "y"))
        self.assertTrue(a.isIsomorphic("aaabbb", "bbbaaa"))

    def test_false(self):
        a = A()
        self.assertFalse(a.isIsomorphic("gge", "add"))
        self.assertFalse(a.isIsomorphic("foo", "bar"))
        self.assertFalse(a.isIsomorphic("bar", "foo"))
