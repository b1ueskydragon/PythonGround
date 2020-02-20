import unittest

from leetcode.p0021.solve import ListNode
from leetcode.p0021.solve import Solution as A


def array_to_list_node(xs):
    root = ListNode(None)
    pos = root
    for x in xs:
        pos.next = ListNode(x)
        pos = pos.next
    return root.next


def compare_list_nodes(l1, l2):
    while l1 and l2:
        if not l1 or not l2:
            return False
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    if l1 or l2:
        return False
    return True


class MergeTwoListsTest(unittest.TestCase):
    def test_compare_list_nodes(self):
        a = A()
        l1 = array_to_list_node([1, 3, 5])
        l2 = array_to_list_node([1, 4, 4])
        expected = array_to_list_node([1, 1])  # give a wrong answer
        self.assertFalse(compare_list_nodes(expected, a.mergeTwoLists(l1, l2)))

    def test_coincident_length_duplicated_element(self):
        a = A()
        l1 = array_to_list_node([1, 3, 5])
        l2 = array_to_list_node([1, 4, 4])
        expected = array_to_list_node([1, 1, 3, 4, 4, 5])
        self.assertTrue(compare_list_nodes(expected, a.mergeTwoLists(l1, l2)))

    def test_same_lengths(self):
        a = A()
        l1 = array_to_list_node(list(range(1, 100, 2)))
        l2 = array_to_list_node(list(range(0, 101, 2)))
        expected = array_to_list_node(list(range(0, 101)))
        self.assertTrue(compare_list_nodes(expected, a.mergeTwoLists(l1, l2)))

    def test_diff_lengths(self):
        a = A()
        l1 = array_to_list_node([1])
        l2 = array_to_list_node([1, 3, 3, 3, 5, 6])
        expected = array_to_list_node([1, 1, 3, 3, 3, 5, 6])
        self.assertTrue(compare_list_nodes(expected, a.mergeTwoLists(l1, l2)))

    def test_both_are_empty(self):
        a = A()
        l1 = array_to_list_node([])
        l2 = array_to_list_node([])
        expected = array_to_list_node([])
        self.assertTrue(compare_list_nodes(expected, a.mergeTwoLists(l1, l2)))

    def test_either_is_empty(self):
        a = A()
        l1 = array_to_list_node([1, 3, 5])
        l2 = array_to_list_node([])
        expected = array_to_list_node([1, 3, 5])
        self.assertTrue(compare_list_nodes(expected, a.mergeTwoLists(l1, l2)))


if __name__ == '__main__':
    unittest.main()
