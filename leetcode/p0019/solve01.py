# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # add a sentinel for prevent RuntimeError on ahead.next
        tmp = ListNode(-1)
        tmp.next = head

        ahead = tmp
        follow = tmp
        while n > 0:
            ahead = ahead.next
            n -= 1
        while ahead.next:
            ahead = ahead.next
            follow = follow.next

        # skip n th
        follow.next = follow.next.next
        return tmp.next
