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
        j = 0
        i = j - n + 1  # Specify the index which be removed.
        while head.next:
            j += 1
            i += 1
            head = head.next
        print(i, j)
