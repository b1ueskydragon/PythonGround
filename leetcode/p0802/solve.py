class Solution:
    def __init__(self):
        self.visited = set()
        self.res = []

    # graph will have length at most 10^4
    # The number of edges in the graph will not exceed 32000
    # Each graph[i] will be a sorted list of different integers
    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        for i, node in enumerate(graph):
            if node == []:
                self.res.append(i)
            else:
                self.has_terminal_node(graph, i)
        return self.res

    def has_terminal_node(self, graph, start):
        end_points = graph[start]
        if end_points == []:
            return True
        for step in end_points:
            if step in self.visited:
                continue
            self.visited.add(start)
            if not self.has_terminal_node(graph, step):
                continue
            self.res.append(start)  # or put first and pop if not
