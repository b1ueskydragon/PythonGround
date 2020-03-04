class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    in-place ?
    """

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        s = head
        f = s.next
        a = acc = ListNode(-1)
        while f:
            if not f.next:
                s.next = None
                f.next = s
                a.next = f
                a = a.next
                s = head
                f = s.next
            else:
                f = f.next
                s = s.next
        return acc.next
