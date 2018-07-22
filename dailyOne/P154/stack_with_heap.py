"""
Implement a stack API using only a heap.
"""


class Stack:
    def __init__(self):
        self.stack = []
        self.heap = Heap()

    def push(self, item):
        """
        adds an element to the stack.
        :param item:
        """
        self.stack.append(item)

    def pop(self):
        """
        removes and returns the most recently added element.
        """
        if not self.stack:
            raise TypeError('nothing on the stack')

        value = self.stack[-1]
        self.stack.remove(value)
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
heap = Heap()
heap.push(3)
heap.push(7)
heap.push(5)
rst = heap.pop()
print(rst)

stack = Stack()
stack.push(2)
stack.push(1)
rst01 = stack.pop()
print(rst01)
