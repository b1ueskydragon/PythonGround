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

    def test_simple_circle(self):
        a = A()
        graph = [[1], [0]]
        expected = []
        self.assertEqual(expected, a.eventualSafeNodes(graph))

    def test_single_element_return_to_itself(self):
        a = A()
        graph = [[0]]
        expected = []
        self.assertEqual(expected, a.eventualSafeNodes(graph))

    def test_has_both_safe_and_circle_1(self):
        a = A()
        graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
        # i=0 has a chance to be a circle
        expected = [4]
        self.assertEqual(expected, a.eventualSafeNodes(graph))

    def test_has_both_safe_and_circle_2(self):
        a = A()
        graph = [[1, 2, 3], [1, 2], [3], [3, 4], []]
        expected = [4]
        self.assertEqual(expected, a.eventualSafeNodes(graph))

    def test_has_a_circle(self):
        a = A()
        graph = [[1, 2, 3], [2, 3], [3, 4], [4, 5], [4], []]
        expected = [5]
        self.assertEqual(expected, a.eventualSafeNodes(graph))

    def test_go_forward_all_except_last(self):
        a = A()
        graph = [[1, 2, 3], [2, 3], [3], []]
        expected = [0, 1, 2, 3]
        self.assertEqual(expected, a.eventualSafeNodes(graph))

    def test_has_a_circle_simple(self):
        a = A()
        graph = [[1, 2], [0], []]
        expected = [2]
        self.assertEqual(expected, a.eventualSafeNodes(graph))
