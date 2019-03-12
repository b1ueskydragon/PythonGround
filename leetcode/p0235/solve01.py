"""
Binary `Search` Tree

same as p0235/solve.py
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# def build(root, curr=None, i=0):
#     import math


def ans(root: Node, p: Node, q: Node) -> Node:
    # base case
    if not root:
        return None

    if root.val > p.val and root.val > q.val:  # lies in left
        return ans(root.left, p, q)

    if root.val < p.val and root.val < q.val:  # lies in right
        return ans(root.right, p, q)

    return root


# root = [20, 8, 22, 4, 12, None, None, None, 10, 14]

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = Node(10)
n2 = Node(14)
print(ans(root, n1, n2).val)  # 12
