# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Apply two points for doing this in one pass.
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # j = 0
        # i = j - n
        # res = ListNode(head.val)
        # point = res
        # while head.next:
        #     j += 1
        #     i += 1
        #     head = head.next
        #     if head:
        #         point.next = head
        #         print(i, j)
        #         point = point.next
        # return res
        p1 = head
        p2 = head
        while n:
            p2 = p2.next
            n -= 1
