import unittest

from leetcode.p0802.solve import Solution as A


class EventualSafeStatesTest(unittest.TestCase):
    def test_basic_balanced_leaf(self):
        a = A()
        graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
        expected = [2, 4, 5, 6]
        self.assertEqual(expected, a.eventualSafeNodes(graph))
