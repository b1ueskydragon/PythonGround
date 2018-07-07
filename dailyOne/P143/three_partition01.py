# TODO another: with BST
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add(self, val):
        if val < self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = Node(val)


def three_partition(x, lst):
    node = Node(x)  # root

    for k in lst:
        node.add(k)

    return node


x, lst = 10, [9, 12, 3, 5, 14, 10, 10]
rst = three_partition(x, lst)
# TODO
