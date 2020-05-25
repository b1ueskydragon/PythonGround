class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left_leaves = 0  # the number of the left-side value the node has.
        self.duplicated = 0  # the number of same value. we want put only one number in the tree even duplicated.
        self.left = None
        self.right = None


class Solution:
    def countSmaller(self, nums: [int]) -> [int]:
        if not nums: return []

        def insert_and_count(root, num):  # make a BST. left is smaller.
            total = 0
            while root.val != num:  # down to the leaf.
                if root.val > num:
                    if not root.left:
                        root.left = TreeNode(num)
                    root.left_leaves += 1
                    root = root.left
                else:
                    if not root.right:
                        root.right = TreeNode(num)
                    total = total + root.left_leaves + root.duplicated
                    root = root.right
            root.duplicated += 1
            return total + root.left_leaves

        N = len(nums)
        res = [0] * N
        last = TreeNode(nums[-1])
        last.duplicated = 1
        for i in reversed(range(N - 1)):
            res[i] = insert_and_count(last, nums[i])
        return res
