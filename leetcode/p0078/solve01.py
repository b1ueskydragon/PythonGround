class Solution:
    """
    Get one head and put two lasts.
    """

    def subsets(self, nums: [int]) -> [int]:
        from collections import deque
        queue = deque()
        queue.append(list())
        i = 0
        while i < len(nums):
            curr = nums[i]
            j = 0
            while j < (1 << i):
                parent = queue.popleft()
                right_child = parent
                left_child = parent + [curr]
                queue.append(left_child)
                queue.append(right_child)
                j += 1
            i += 1

        return list(queue)
