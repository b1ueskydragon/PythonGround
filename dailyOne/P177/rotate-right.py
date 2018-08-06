class Node:
    """
    a node holds an element (value),
    and two pointers (prev, next)
    """

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None

    def add_last(self, el):
        """
        link non-null node as last
        """
        tmp_lst = self.last  # keep current last
        node = Node(el)  # new Node
        self.last = node
        if not tmp_lst:
            self.head = node
        else:
            self.last.prev = tmp_lst
            tmp_lst.next = node
        self.size += 1

    def remove_and_get_element(self):
        """
        unlink non-null node
        and get last value before removed
        """
        if not self.last:
            raise NotImplementedError('Empty list')
        else:
            tmp = self.last
            if not tmp.prev:  # self.size is 1
                self.head = None
            else:
                self.last = tmp.prev
                self.last.next = None
            self.size -= 1
        return tmp.value

    def add_first(self, el):
        """
        link non-null node as first
        """
        tmp_head = self.head  # keep current head
        node = Node(el)  # new Node
        self.head = node
        if not tmp_head:
            self.last = node
        else:
            tmp_head.prev = node
            self.head.next = tmp_head
        self.size += 1


if __name__ == '__main__':
    given = LinkedList()
    size = int(input())
    for _ in range(size):
        given.add_last(int(input()))
    k = int(input())


    def output_datum(nodes):
        out = []
        node = nodes.head
        while node:
            out.append(node.value)
            node = node.next
        print(out)


    output_datum(given)

    for _ in range(k):
        given.add_first(given.remove_and_get_element())

    output_datum(given)
