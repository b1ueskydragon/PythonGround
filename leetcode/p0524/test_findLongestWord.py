import unittest
from leetcode.p0524.solve import Solution as A


class FindLongestWordTest(unittest.TestCase):
    def test_return_the_longest_word(self):
        a = A()
        s = "abpcplea"
        d = ["ale", "apple", "monkey", "plea"]

        expected = "apple"
        self.assertEqual(expected, a.findLongestWord(s, d))

    def test_return_empty_when_no_possible_result(self):
        a = A()
        s = "abpcplea"
        d = ["x", "y", "z"]

        expected = ""
        self.assertEqual(expected, a.findLongestWord(s, d))

    def test_return_the_smallest_lexicographical_order_when_more_than_one_possible_result(self):
        a = A()
        s = "abpcplea"
        d = ["a", "b", "c"]

        expected = "apple"
        self.assertEqual(expected, a.findLongestWord(s, d))


if __name__ == '__main__':
    unittest.main()
