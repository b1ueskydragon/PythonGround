# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Given a binary tree, flatten it to a linked list in-place.
        Do not return anything, modify root in-place instead.
        """


if __name__ == '__main__':
    root = [1, 2, 5, 3, 4, None, 6]
    expected = [1, None, 2, None, 3, None, 4, None, 5, None, 6]
