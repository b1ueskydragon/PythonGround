import unittest

from leetcode.p0802.solve import Solution as A


class EventualSafeStatesTest(unittest.TestCase):
    def test_sample(self):
        a = A()
        graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
        expected = [2, 4, 5, 6]
        self.assertEqual(expected, a.eventualSafeNodes(graph))

    def test_sample_node_4_goes_back(self):
        a = A()
        graph = [[1, 2], [2, 3], [5], [0], [2], [], []]
        expected = [2, 4, 5, 6]
        self.assertEqual(expected, a.eventualSafeNodes(graph))
