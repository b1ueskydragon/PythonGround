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

        pp, qp = pair[p], pair[q]
        ans_p, ans_q = [p], [q]
        while pp:
            ans_p.append(pp)
            pp = pair[pp]
        while qp:
            ans_q.append(qp)
            qp = pair[qp]

        while len(ans_p) > len(ans_q):
            ans_p.pop(0)
        while len(ans_q) > len(ans_p):
            ans_q.pop(0)

        for i, lcp in enumerate(ans_p):
            if ans_q[i] == lcp:
                return lcp
        return None
