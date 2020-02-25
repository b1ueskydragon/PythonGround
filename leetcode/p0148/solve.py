class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode):
        p = res = ListNode(None)  # sentinel
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2
        return res.next

    def sortList(self, head: ListNode) -> ListNode:
        # exit case: length is less than 2.
        if not head or not head.next:
            return head

        # standard case: split to two lists (from last to head).
        prev = None
        p1 = p2 = head
        while p2 and p2.next:
            prev = p1
            p1 = p1.next
            p2 = p2.next.next

        prev.next = None  # make a head as a left-half (same object).

        return Solution.mergeTwoLists(self.sortList(head), self.sortList(p1))
