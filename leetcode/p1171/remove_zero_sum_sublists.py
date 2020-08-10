class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        cur = ListNode()
        cur.next = head
        sum_map = dict()  # update to the farthest node
        acc = 0
        while cur:
            acc += cur.val
            sum_map[acc] = cur
            cur = cur.next

        res = ListNode()
        res.next = head
        curr = res
        total = 0
        while curr:
            total += curr.val
            if total in sum_map:
                curr.next = sum_map[total].next
            curr = curr.next
        return res.next
