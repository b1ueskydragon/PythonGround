import unittest
from leetcode.p0524.solve import Solution as A
from leetcode.p0524.solve01 import Solution as B


class FindLongestWordTest(unittest.TestCase):
    def test_return_the_longest_word(self):
        a, b = A(), B()
        s = "abpcplea"
        d = ["ale", "apple", "monkey", "plea"]

        expected = "apple"
        self.assertEqual(expected, a.findLongestWord(s, d))
        self.assertEqual(expected, b.findLongestWord(s, d))

    def test_return_empty_when_no_possible_result(self):
        a, b = A(), B()
        s = "abpcplea"
        d = ["x", "y", "z"]

        expected = ""
        self.assertEqual(expected, a.findLongestWord(s, d))
        self.assertEqual(expected, b.findLongestWord(s, d))

    def test_return_the_smallest_lexicographical_order_when_more_than_one_possible_result(self):
        a, b = A(), B()
        s = "abpcplea"
        d = ["a", "b", "c"]

        expected = "a"
        self.assertEqual(expected, a.findLongestWord(s, d))
        self.assertEqual(expected, b.findLongestWord(s, d))

    def test_monkey(self):
        a, b = A(), B()
        s = "momonmonkeykeynkey"
        d = ["mon", "plea", "mon", "momokyyk", "key", "onmky", "kyk"]

        expected = "momokyyk"
        self.assertEqual(expected, a.findLongestWord(s, d))
        self.assertEqual(expected, b.findLongestWord(s, d))

    def test_only_two_type_chars(self):
        a, b = A(), B()
        s = "bab"
        d = ["ba", "ab", "a", "b"]

        expected = "ab"
        self.assertEqual(expected, a.findLongestWord(s, d))
        self.assertEqual(expected, b.findLongestWord(s, d))

    def test_only_contains_head_elements(self):
        a, b = A(), B()
        s = "aewfafwafjlwajflwajflwafj"
        d = ["apple", "ewaf", "awefawfwaf", "awef", "awefe", "ewafeffewafewf"]
        expected = "ewaf"
        self.assertEqual(expected, a.findLongestWord(s, d))
        self.assertEqual(expected, b.findLongestWord(s, d))


if __name__ == '__main__':
    unittest.main()
