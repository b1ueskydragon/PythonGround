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

# TODO add function for print tree
print(rst.value)  # 10
print(rst.left.value)  # 9
print(rst.left.left.value)  # 3
print(rst.left.left.right.value)  # 5
print(rst.right.value)  # 12
print(rst.right.left.value)  # 10
print(rst.right.right.value)  # 14
