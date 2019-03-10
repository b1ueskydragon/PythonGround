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
    # additional O(N) space
    queue = deque([root])

    # All of the nodes' values will be unique. {curr : parent}
    # init is root and itself
    pair = {root: root}

    # BFS; O(N) time traversal from root
    while queue:
        curr = queue.popleft()
        if curr.left:
            pair[curr.left] = curr
            queue.append(curr.left)  # if pop a parent, child be None too, so, revert
        if curr.right:
            pair[curr.right] = curr
            queue.append(curr.right)

    # connect
    pp = p
    qq = q
    parents = set()  # use O(1) time; Since All of the nodes' values will be unique.
    while pair:
        if pp in pair:
            if pp in parents:
                return pp
            parents.add(pp)
            pp = pair[pp]

        if qq in pair:
            if qq in parents:
                return qq
            parents.add(qq)
            qq = pair[qq]


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

print(ans(root, p=root.left.right.left, q=root.left.right.right).val)  # root=3, p=7, q=4 ans=2
print(ans(root, p=root.left.right.right, q=root.left).val)  # 5
print(ans(root, p=root, q=root.left.right.left).val)  # 3
print(ans(root, p=root.left.left, q=root.left.right.right).val)  # 5
print(ans(root, p=root.right, q=root.left).val)  # 3
