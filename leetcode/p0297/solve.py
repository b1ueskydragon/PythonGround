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
        lq = deque()
        rq = deque()
        data_list = Codec.str2list(data)
        for i, data in enumerate(data_list):
            if i % 2 != 0:
                lq.append(data)
            else:
                rq.append(data)

        root = TreeNode(rq.popleft())

        def dfs(root):
            if lq:
                lv = lq.popleft()
                if lv:
                    root.left = TreeNode(lv)
                    dfs(root.left)
                else:
                    return
            if rq:
                rv = rq.popleft()
                if rv:
                    root.right = TreeNode(rv)
                    dfs(root.right)
                else:
                    return

        dfs(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
