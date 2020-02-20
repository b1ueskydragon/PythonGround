class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        min_int = -2147483648
        res = ListNode(min_int)
        pres = res  # position
        while l1 and l2:
            if l1.val < l2.val:
                pres.next = l1
                l1 = l1.next
            else:
                pres.next = l2
                l2 = l2.next
            pres = pres.next
        # flush
        while l1:
            pres.next = l1
            l1 = l1.next
            pres = pres.next
        while l2:
            pres.next = l2
            l2 = l2.next
            pres = pres.next
        return res.next
