class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#                         X
# a1, a2, ... ,  an-k,  an-k+1 , ... , an
#                 [p]                 [p+k]
#                 slow                fast
#
# an-k+1           : k th from the end
# [a1      ..an-k] : length n-k
# [an-k+1  ..  an] : length k
def remove_nth_from_end(self, head: ListNode, k: int):
    fast = slow = head
    while k > 0:
        if not fast.next:
            return head.next
        fast = fast.next
        k -= 1
    if not fast:
        return None
    while fast:
        if not fast.next:  # fast reaches the end.
            slow.next = slow.next.next
            break
        fast = fast.next
        slow = slow.next
    return head
