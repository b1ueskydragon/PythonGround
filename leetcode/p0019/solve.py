from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 0
        root = head
        while root:
            root = root.next
            size += 1
        k = 0
        index = size - n
        if index == 0:
            head = head.next
        if not head:
            return None
        res = ListNode(head.val)
        q = deque([res])
        while q and head.next:
            k += 1
            node = q.popleft()
            if k == index:
                head.next = head.next.next
            if head.next:
                node.next = ListNode(head.next.val)
                q.append(node.next)
                head = head.next
        return res
        # TODO: two points
