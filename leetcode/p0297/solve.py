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
                if len(q) % 2 != 0 and all(not v for v in q):
                    break
                res += f'null, '
        return f'[{res[:-2]}]'

    @staticmethod
    def str2list(data_str):
        return [None if v == 'null' else int(v) for v in data_str[1:-1].split(", ")]

    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = Codec.str2list(data)
        if data_list[0] is None:
            return []  # edge case
        root = TreeNode(data_list[0])
        q = deque([root])
        pos = 1
        while q and len(data_list) > pos:
            parent = q.popleft()
            if data_list[pos] is not None:
                parent.left = TreeNode(data_list[pos])
                q.append(parent.left)
            pos += 1
            if data_list[pos] is not None:
                parent.right = TreeNode(data_list[pos])
                q.append(parent.right)
            pos += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
