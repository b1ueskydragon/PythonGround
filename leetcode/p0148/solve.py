class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        pos = head
        pivot_v, n = 0, 0
        # O(N) to find a pivot
        while pos:
            pivot_v += pos.val
            n += 1
            pos = pos.next
        pivot_v //= n

        print(pivot_v)

        # O(logN) to sorting
        p1 = p2 = head
