class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(N) space to save execution time.
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
