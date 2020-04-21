class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        a = head
        loop = n - m
        while m > 1:
            a = a.next
            m -= 1

        res = None
        while loop >= 0:
            an = a.next
            a.next = res
            res = a
            a = an
            loop -= 1

        if not head.next:
            head = res
        else:
            h = head
            b = head.next
            while b.next:
                b = b.next
                h = h.next
            h.next = res

        c = res
        while c.next:
            c = c.next
        c.next = a

        return head
