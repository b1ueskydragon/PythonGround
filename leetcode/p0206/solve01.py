class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionA:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev, follow = None, head.next
        while head:
            head.next = prev
            prev = head
            head = follow
            if follow:
                follow = follow.next
        return prev


class SolutionB:
    # Start with next is also OK. So, return should be head instead of prev.
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev, follow = None, head.next
        while follow:
            follow = head.next
            head.next = prev
            if follow:
                prev = head
                head = follow
        return head
