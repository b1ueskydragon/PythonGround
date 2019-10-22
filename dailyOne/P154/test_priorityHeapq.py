from unittest import TestCase
from dailyOne.P154 import stack_with_heapq as hq


class TestPriorityHeapq(TestCase):
    """
    TODO: Priority Heap Test
        phq = PriorityHeapq()
        phq.push('c', 0)
        print(phq.heap)  # [(0, 'c')]
        phq.push('a', 1)
        print(phq.heap)  # [(-1, 'a'), (0, 'c')]
        phq.push('b', 2)
        print(phq.heap)  # [(-2, 'b'), (0, 'c'), (-1, 'a')]
        print(phq.pop())  # b
        print(phq.heap)  # [(-1, 'a'), (0, 'c')]
    """

    def test_stack(self):
        stack = hq.Stack()
        stack.push('c')
        stack.push('a')
        stack.push('b')

        print(stack.phq.heap)

        self.assertEqual('b', stack.pop())
        self.assertEqual('a', stack.pop())
        self.assertEqual('c', stack.pop())
        self.assertEqual([], stack.phq.heap)

    def test_empty_stack(self):
        stack = hq.Stack()
        with self.assertRaises(IndexError):
            stack.pop()
