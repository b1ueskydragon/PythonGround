from collections import deque


class Solution:
    """
                 0
              /+1  \+2
            1           2
         /+1  \+2    /+1  \+2
        2      3     3     4
    """

    def climbStairs(self, n: int) -> int:
        queue = deque([0])
        size = 1
        count = 0
        while True:
            if queue[0] > n:
                break
            for _ in range(size):
                parent = queue.popleft()
                for edge in range(1, 3):
                    child = edge + parent
                    if child == n:
                        count += 1
                    queue.append(child)
            size = len(queue)
        return count
