"""
 leaf nodes are always unival trees
"""


# each node of a tree
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_node(self):
        return self.data


def a_tree():
    tree = Node(5)  # root node
    tree.left = Node(5)
    tree.left.left = Node(5)
    tree.left.right = Node(5)
    tree.right = Node(5)
    tree.right.right = Node(5)
    return tree


def tree_sum(tree):
    if tree is None:
        return 0
    return tree.get_node() + tree_sum(tree.left) + tree_sum(tree.right)


print(tree_sum(a_tree()))
