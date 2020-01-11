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
        # i = 0 - n
        # res = ListNode(head.val)
        # point = res
        # while head.next:
        #     i += 1
        #     head = head.next
        #     if head:
        #         point.next = head
        #         point = point.next
        #         if not head.next:
        #             # get the i for left side
        #             # point for right side
        #             break
        #
        # # TODO: complete. this is a WIP
        # left = res
        # # print(point)
        # while i > 0:
        #     left = left.next
        #     i -= 1
        # else:
        #     left.next = point
        # return res

        p1 = head
        p2 = head
        while n:
            p2 = p2.next
            n -= 1
