class Node:
    def __init__(self, val, prev: 'Node', next: 'Node', child: 'Node'):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    # TODO: we should concat child first then next
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        branch = None
        if head.next:
            if head.child:
                branch = head.child  # concat when reached the end
                head.child = None
            self.flatten(head.next)  # go to the next anyway
            self.flatten(branch)  # if has child, should be go deeper and do same thing
            tmp_head = head
            while head.next:
                head = head.next
            else:
                if branch:
                    branch.prev = head
                    head.next = branch
            head = tmp_head  # revert
        return head
