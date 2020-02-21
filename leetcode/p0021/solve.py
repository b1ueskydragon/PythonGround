class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = pres = ListNode(None)  # pres is a position
        while l1 and l2:
            if l1.val < l2.val:
                pres.next = l1
                l1 = l1.next
            else:
                pres.next = l2
                l2 = l2.next
            pres = pres.next
        pres.next = l1 or l2  # flush
        return res.next
