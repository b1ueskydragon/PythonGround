import unittest
from leetcode.p0078.solve import Solution as DFS
from leetcode.p0078.solve01 import Solution as BFS


class SubSetsCase(unittest.TestCase):
    def test_order_dfs(self):
        a = DFS()

        nums = [1, 2, 3]
        expected = [
            [3, 2, 1],
            [2, 1],
            [3, 1],
            [1],
            [3, 2],
            [2],
            [3],
            []
        ]

        self.assertEqual(expected, a.subsets(nums))

    def test_order_bfs(self):
        b = BFS()

        nums = [1, 2, 3]
        expected = [
            [1, 2, 3],
            [1, 2],
            [1, 3],
            [1],
            [2, 3],
            [2],
            [3],
            []
        ]

        self.assertEqual(expected, b.subsets(nums))


if __name__ == '__main__':
    unittest.main()
