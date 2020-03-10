"""
Recursion, not a tailrec. but fast.
O(N) Time, O(N) implicit stack Space due to recursion (N level deep).
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        follow = self.reverseList(head.next)
        head.next.next = head  # 4->5->N, if head points 4 and follow points 5. 4->5->4->...(circle)
        head.next = None  # cut a circle. 4  5->4
        return follow  # return to reuse result
