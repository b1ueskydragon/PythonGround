"""
leaf nodes can be unival tree too
"""


# each node of a tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_node(self):
        return self.value


def a_tree():
    tree = Node(5)  # root node
    tree.left = Node(5)
    tree.left.left = Node(5)
    tree.left.right = Node(5)
    tree.right = Node(5)
    tree.right.right = Node(5)
    return tree


def b_tree():
    tree = Node('a')  # root node
    tree.left = Node('c')
    tree.right = Node('b')
    tree.right.left = Node('b')
    tree.right.right = Node('b')
    tree.right.right.right = Node('b')
    return tree


"""
def tree_sum(tree):
    if tree is None:
        return 0
    else:
        return tree.get_node() + tree_sum(tree.left) + tree_sum(tree.right)


print(tree_sum(a_tree()))
"""


def is_unival(tree):  # basic case is root
    return tree_count(tree, tree.value)


def tree_count(tree, value):
    if tree is None:
        return True
    if tree.value == value:
        return tree_count(tree.left, value) and tree_count(tree.right, value)
    return False


rootA = a_tree()
print(is_unival(rootA))
rootB = b_tree()
print(is_unival(rootB))

