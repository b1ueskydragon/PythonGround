"""
Implements of Simply Binary Search Tree(二分探索木).
"""


class BinaryNode:
    def __init__(self, value=None):
        """二分節点を作る"""
        self.value = value
        self.left = None
        self.right = None

    def add(self, val):
        """この値を含む新しい接点を二分探索木に追加する"""
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)


class BinaryTree:
    def __init__(self):
        """空の二分探索木を作る"""
        self.root = None

    def add(self, value):
        """二分探索木のしかるべき位置に値を挿入する"""
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)
