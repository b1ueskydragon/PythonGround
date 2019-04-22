"""
Recursively
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return


if __name__ == '__main__':
    s = Solution()
    print(s.isSymmetric(root=[1, 2, 2, 3, 4, 4, 3]))
