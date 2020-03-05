class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """ O(N) speed, O(1) space. """

    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
