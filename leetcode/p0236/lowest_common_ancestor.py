from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # All of the nodes' values will be unique.
    # p and q are different and both values will exist in the binary tree.
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pair = dict()  # curr : parent
        pair[root] = None
        path = deque([root])
        while path:
            curr = path.popleft()
            if curr.left:
                path.append(curr.left)
                pair[curr.left] = curr
            if curr.right:
                path.append(curr.right)
                pair[curr.right] = curr

        ans = set()
        while q:  # start with q or p either is ok.
            ans.add(q)
            q = pair[q]
        while p not in ans:  # the first appear will be an lcp.
            p = pair[p]
        return p
