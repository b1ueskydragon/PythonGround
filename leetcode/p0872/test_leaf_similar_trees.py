import unittest

from leetcode.p0872.solve import Solution as A
from leetcode.p0872.solve import TreeNode as Node


class IntToRomanTest(unittest.TestCase):
    """
    case 1
    [3,5,1,6,2,9,10,null,null,7,4]
    [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]

    case 2
    [1,null,2,null,3,null,6, 5, 4]
    [1,2,null,3,6,null,4,null, 5]


    case 3
    [1,null,2,null,3,null,4]
    [1,2,null,3,null,4]

    case 4 --- TODO
    [44,79,25,null,null,112,7,74,49,2,122]
    [38,86,120,49,54,2,122,null,null,74,79]
    """

    def test_same_direction_diff_depth(self):
        a = A()
        root1 = Node(3)
        root1 = Node(5)

        root2 = Node(3)
        root2.left = Node(5)
        root2.right = Node(1)
        root2.left.left = Node(6)
        root2.left.right = Node(7)
        root2.right.left = Node(4)
        root2.right.right = Node(2)
        root2.right.right.left = Node(9)
        root2.right.right.right = Node(8)

        self.assertTrue(a.leafSimilar(root1, root2))
