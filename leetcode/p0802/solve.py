class Solution:
    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        res = set()
        visited = set()

        def is_terminal_node(start):
            if start in res:
                return True
            if start in visited:
                return False
            visited.add(start)
            for step in graph[start]:
                if not is_terminal_node(step):
                    return False
            res.add(start)
            return True

        for node in range(len(graph)):
            if node not in visited:
                is_terminal_node(node)
        return sorted(res)
