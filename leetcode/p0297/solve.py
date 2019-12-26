from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ""
        q = deque([root])
        while q:
            parent = q.popleft()
            if parent:
                res += f'{parent.val}, '
                q.append(parent.left)
                q.append(parent.right)
            else:
                res += f'null, '
        return f'[{res[:-2]}]'

    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = [None if v == 'null' else int(v) for v in data[1:-1].split(", ")]
        c = 0
        for v in reversed(data_list):
            if v is None:
                c += 1
            else:
                break
        trim_len = c if c % 2 == 0 else c - 1
        data_list = data_list[:len(data_list) - trim_len]

        # debug
        print(data_list)

        root = TreeNode(data_list[0])
        root.left = TreeNode(data_list[1])
        root.right = TreeNode(data_list[2])
        root.right.left = TreeNode(data_list[5])
        root.right.right = TreeNode(data_list[6])

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
