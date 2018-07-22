"""
Implement a stack API using only a heap.

(memo) most recently := largest
"""


class Stack:
    def __init__(self):
        self.key = Heap()
        self.idx = 0
        self.stack = []

    def push(self, item):
        """
        adds an element to the stack.
        :param item:
        """
        self.key.push(self.idx)
        self.stack.append(item)
        self.idx += 1

    def pop(self):
        """
        removes and returns the most recently added element.
        """
        if not self.key or not self.stack:
            raise TypeError('nothing on the stack')

        value = self.stack[self.key.pop()]
        self.stack.remove(value)
        self.idx -= 1

        return value


class Heap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        """
        adds a new key to the heap.

        :param item:
        """
        self.heap.append(item)

    def pop(self):
        """
        removes and returns the max value of the heap.
        """
        value = max(self.heap)
        self.heap.remove(value)
        return value


# Test
# heap = Heap()
# heap.push(3)
# heap.push(7)
# heap.push(5)
# rst = heap.pop()
# print(rst)

stack = Stack()
stack.push(2)
stack.push(1)
rst01 = stack.pop()
print(rst01)
stack.push(3)
stack.push(4)
rst02 = stack.pop()
print(rst02)
print(stack.stack)
