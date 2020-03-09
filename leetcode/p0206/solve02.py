"""
Recursive implementation.

O(N) time and additional O(N) space,
since Python doesn't have tailrec optimization(or elimination), stacks will be accumulated on each step.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionA:
    def reverseList(self, head: ListNode) -> ListNode:
        def _rec(head: ListNode, res: ListNode):
            if not head:
                return res
            follow = head.next
            head.next = res  # res is prev
            return _rec(follow, head)

        return _rec(head, None)


class SolutionB:
    prev = None

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return self.prev
        follow = head.next
        head.next = self.prev
        self.prev = head
        return self.reverseList(follow)
