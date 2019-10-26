class Node:
    def __init__(self, val, prev: 'Node', next: 'Node', child: 'Node'):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        branch = None
        if head.next:
            if head.child:
                branch = head.next
                head.child.prev = head
                head.next = head.child
                head.child = None
        else:  # no next but only has children
            if head.child:
                head.next = head.child
                head.next.prev = head
                head.child = None
        self.flatten(head.next)
        self.flatten(branch)
        tmp_head = head
        while head.next:
            head = head.next
        else:
            if branch:
                if head:
                    branch.prev = head
                head.next = branch
        head = tmp_head  # revert
        return head
