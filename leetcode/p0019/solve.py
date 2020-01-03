# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from collections import deque


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        k = 0
        res = ListNode(head.val)
        q = deque([res])
        while q and head.next:
            node = q.popleft()
            node.next = ListNode(head.next.val)
            q.append(node.next)
            head = head.next
            k += 1
        print(k)
        return res
        # TODO: fix wip
        # TODO: two points
