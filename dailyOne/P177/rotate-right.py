class Node:
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
        tmp_lst = self.last
        node = Node(el)
        self.last = node
        if not tmp_lst:
            self.head = node
        else:
            tmp_lst.next = node
        self.size += 1


given = LinkedList()
given.add_last(5)
given.add_last(4)
given.add_last(3)

print(given.head.next.next.value)
