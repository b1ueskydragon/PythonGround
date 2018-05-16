def reverse(head, prev=None):  # clean up prev pointer first at each recursion
    """
    reverse a singly linked list in-place.
    O(N) time + O(N) space.
    Since there is no tail-recursion in python.

    :param head: a current head. refers to the first node of the list.
    :param prev: a previous element of the current head.
    :return:
    """
    if not head:  # head is empty == end of searching
        return prev

    tmp = head.next  # keep the current `next` for next recursion (current next would be next head)
    head.next = prev  # now head.next refers previous element of current head
    return reverse(tmp, head)  # (next head, prev of next head)


def reverse_ite(head):
    """
     improve the space by doing iteratively.
     only use constant space.

    :param head: init head
    :return:
    """
    prev = None
    curr = head

    while curr is not None:
        tmp = head.next
        head.next = prev
        prev = curr
        curr = tmp

    return prev
