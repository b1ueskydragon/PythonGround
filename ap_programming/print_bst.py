"""
Visualization exist BST
"""


# TODO
def print_tree(node):
    if node:
        print(node.value)
        if node.left:
            print_tree(node.left)
        if node.right:
            print_tree(node.right)

# def print_tree(node: Node):
#     if node:
#         print(' ' + revert(node.codes))
#     if node.left:
#         blank = ''.join([' ' for _ in range(len(revert(node.codes)) - 1)])
#         print('/' + blank + '\\')
#         blank = ''.join([' ' for _ in range(len(revert(node.codes)) // 3)])
#         print(revert(node.left.codes) + blank + revert(node.right.codes))
#     if node.right:
#         print()
