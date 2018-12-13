class LinkedNode:
    """ A node of an LinkedList """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def solve(headernode):
    """
    :param headernode: head node of linked node(s)
    """
    head = headernode

    while head:
        """ init """
        node = head
        acc = 0
        skip = False

        while node:  # has next
            acc += node.value
            if acc == 0:
                head = node
                skip = True
                break

            node = node.next

        if not skip:
            print(head.value)

        head = head.next


node0 = LinkedNode(5)
node1 = LinkedNode(-6)
node2 = LinkedNode(6)
node3 = LinkedNode(7)

node0.next = node1
node1.next = node2
node2.next = node3

solve(node0)

a = LinkedNode(1)
b = LinkedNode(2)
c = LinkedNode(3)
d = LinkedNode(4)
e = LinkedNode(-3)
f = LinkedNode(-1)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

solve(a)
