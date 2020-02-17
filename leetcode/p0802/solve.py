class Solution:
    def __init__(self):
        self.visited = set()  # memoing all of visited start and step point
        self.res = set()
        self.has_circle = set()

    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        for i, node in enumerate(graph):
            if node == []:
                self.res.add(i)
            else:
                self.has_terminal_node(graph, i, i)
        return list(self.res - self.has_circle)

    def has_terminal_node(self, graph, root, start):
        end_points = graph[start]
        if end_points == []:
            return True
        for step in end_points:
            if start in self.visited and step in self.visited:
                print(self.res, root, start, step)
                if start == step:
                    self.has_circle.add(root)
                continue
            if step in self.res:
                self.res.add(start)
                continue
            self.visited.add(step)
            if self.has_terminal_node(graph, root, step):
                self.res.add(start)
