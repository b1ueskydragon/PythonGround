class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0: return 0
        edges = [i * i for i in range(1, int(n ** 0.5) + 1)]
        visited = [False] * (n + 1)
        level = 0  # min count
        parents = [0]  # to construct first level (count `1`)
        while parents:
            level += 1
            children = []
            for parent in parents:
                for edge in edges:
                    child = parent + edge
                    if child > n:
                        break
                    if child == n:
                        return level
                    if not visited[child]:
                        visited[child] = True
                        children.append(child)  # only append if not visited
            parents = children  # children become to next parents
