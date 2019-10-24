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
        if head.next:
            if head.child:
                branch = head.child  # concat when reached the end
                head.child = None
            self.flatten(head.next)  # go to the next anyway
        return head
