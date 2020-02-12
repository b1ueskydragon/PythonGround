class Solution:
    def __init__(self):
        self.visited = set()  # memoing all of visited start and step point
        self.res = set()

    # graph will have length at most 10^4
    # The number of edges in the graph will not exceed 32000
    # Each graph[i] will be a sorted list of different integers
    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        for i, node in enumerate(graph):
            if node == []:
                self.res.add(i)
            else:
                self.has_terminal_node(graph, i)
        return list(self.res)

    def has_terminal_node(self, graph, start):  # too many side-effects
        end_points = graph[start]
        if end_points == []:
            return True
        for step in end_points:
            if start in self.visited and step in self.visited:
                continue
            if step in self.res:
                self.res.add(start)  # visited and proper
                continue
            self.visited.add(step)
            if self.has_terminal_node(graph, step):
                self.res.add(start)
