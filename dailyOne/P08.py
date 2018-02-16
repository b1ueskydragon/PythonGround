# each node of a tree
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def add_tree():
    tree = Node(4)  # root node
    tree.left = Node(3)
    tree.right = Node(5)
    return tree


add_tree()
