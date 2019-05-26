import unittest
from leetcode.p0997.solve import Solution as Solve
from leetcode.p0997.solve01 import Solution as Solve1
from leetcode.p0997.solve02 import Solution as Solve2


class FindJudgeTest(unittest.TestCase):
    s, s1, s2 = Solve(), Solve1(), Solve2()

    def test_findJudge_judge_three_people(self):
        N = 3
        trust = [[1, 3], [2, 3], [2, 1]]

        expected = 3

        self.assertEqual(expected, self.s.findJudge(N, trust))
        self.assertEqual(expected, self.s1.findJudge(N, trust))
        self.assertEqual(expected, self.s2.findJudge(N, trust))

    def test_findJudge_judge_four_people(self):
        N = 4
        trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]

        expected = 3

        self.assertEqual(expected, self.s.findJudge(N, trust))
        self.assertEqual(expected, self.s1.findJudge(N, trust))
        self.assertEqual(expected, self.s2.findJudge(N, trust))

    def test_findJudge_empty(self):
        N = 1
        trust = []

        expected = 1

        self.assertEqual(expected, self.s.findJudge(N, trust))
        self.assertEqual(expected, self.s1.findJudge(N, trust))
        self.assertEqual(expected, self.s2.findJudge(N, trust))

    def test_findJudge_judge_only_two_people(self):
        N = 2
        trust = [[1, 2]]

        expected = 2

        self.assertEqual(expected, self.s.findJudge(N, trust))
        self.assertEqual(expected, self.s1.findJudge(N, trust))
        self.assertEqual(expected, self.s2.findJudge(N, trust))

    def test_findJudge_judge_trust_someone(self):
        N = 3
        trust = [[1, 3], [2, 3], [3, 1]]

        expected = -1

        self.assertEqual(expected, self.s.findJudge(N, trust))
        self.assertEqual(expected, self.s1.findJudge(N, trust))
        self.assertEqual(expected, self.s2.findJudge(N, trust))

    def test_findJudge_judge_not_enough_trust(self):
        N = 3
        trust = [[1, 2], [2, 3]]  # 1->3 not exists

        expected = -1

        self.assertEqual(expected, self.s.findJudge(N, trust))
        self.assertEqual(expected, self.s1.findJudge(N, trust))
        self.assertEqual(expected, self.s2.findJudge(N, trust))


if __name__ == '__main__':
    unittest.main()
