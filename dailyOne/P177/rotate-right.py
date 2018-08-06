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
        node = Node(el)  # new Node
        self.last = node
        if not tmp_lst:
            self.head = node
        else:
            self.last.prev = tmp_lst
            tmp_lst.next = node
        self.size += 1

    def remove_and_get_last(self):
        if not self.last:
            raise NotImplementedError
        else:
            tmp = self.last
            self.last = None
            self.size -= 1
        return tmp


if __name__ == '__main__':
    given = LinkedList()

    # TODO impl with input
    given.add_last(1)
    given.add_last(2)
    given.add_last(3)
    given.add_last(4)
    given.add_last(5)
    k = 3
    # 1,2,3,4,5 (ori)

    # 5,1,2,3,4
    # 4,5,1,2,3
    # 3,4,5,1,2 (res)
    print(given.head.next.prev.next.next.prev.prev is given.head)