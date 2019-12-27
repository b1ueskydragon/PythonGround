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
        q = deque(data_list)
        root = TreeNode(q.popleft())

        #              1
        #     2   ,  3    , 4,     5,       1 ~ 2  2 * (2**1 -1)    + 1
        #   6, 7,  8 , 9, 10, 11, 12, 13    5 ~ 8  2 * (2**2 -1)    + 3
        #  14        20,21                  13 ~20 2 * (2**3 -1)    + 7
        # 30                                29 ~   2 * (2**4 -1)    + 15
        test = data_list[1:]
        lq = deque()
        for i, v in enumerate(test, start=1):
            a = 2 * (2 ** i - 1) - 1
            b = a + 2 ** i
            print(a, b)
            if b > len(data_list):
                break

        def dfs(root):
            if root:
                if q:
                    root.left = TreeNode(q.popleft())
                    root.right = TreeNode(q.popleft())
                dfs(root.left)

        dfs(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
