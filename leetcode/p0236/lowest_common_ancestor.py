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
        pair[root.val] = None
        path = deque([root])
        while path:
            curr = path.popleft()
            if curr.left:
                path.append(curr.left)
                pair[curr.left.val] = curr.val
            if curr.right:
                path.append(curr.right)
                pair[curr.right.val] = curr.val

        pp = pair[p.val]
        ps = [p.val]
        while pp is not None:
            ps.append(pp)
            pp = pair[pp]

        qp = pair[q.val]
        qs = [q.val]
        while qp is not None:
            qs.append(qp)
            qp = pair[qp]

        while len(ps) > len(qs):
            ps.pop(0)
        while len(qs) > len(ps):
            qs.pop(0)

        for i, v in enumerate(ps):
            if qs[i] == v:
                return TreeNode(v)
        return None
