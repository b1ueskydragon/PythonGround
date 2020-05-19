"""
To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.

memo:
Recall that a pos is for just representation, since representing a cycle on the code is a bit(?) complex.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(1) space
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while fast:
            if slow == fast:  # meet eventually if has cycle. since fast is two times faster than slow.
                return True
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:  # no more next to proceed. since there's no cycle.
                return False
        return False
