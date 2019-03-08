"""
Binary Tree
"""

from collections import deque


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def ans(root: Node, p: Node, q: Node) -> Node:
    if p.val == root.val or q.val == root.val:
        return root.val

    queue = deque([root])  # additional O(N) space
    pair = {}  # All of the nodes' values will be unique. {curr : parent}

    # BFS; O(N) time traversal from root
    while queue:
        curr = queue.popleft()
        if curr.left:
            pair[curr.left.val] = curr
            queue.append(curr.left)  # if pop a parent, child be None too, so, revert
        if curr.right:
            pair[curr.right.val] = curr
            queue.append(curr.right)

    # connect
    pp = p
    qq = q
    parents = set()  # use O(1) time; Since All of the nodes' values will be unique.
    while pair:
        if pp.val in pair:
            if pp.val in parents:
                return pp.val
            parents.add(pp.val)
            pp = pair[pp.val]

        if qq.val in pair:
            if qq.val in parents:
                return qq.val
            parents.add(qq.val)
            qq = pair[qq.val]


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

print(ans(root, p=Node(7), q=Node(4)))
print(ans(root, p=Node(4), q=Node(5)))
print(ans(root, p=Node(3), q=Node(7)))
print(ans(root, p=Node(6), q=Node(4)))
print(ans(root, p=Node(1), q=Node(5)))  # !
