from unittest import TestCase

from dailyOne.P154 import stack_with_heapq as hq


class TestPriorityHeapq(TestCase):
    def test_priority_heap_queue(self):
        queue = hq.PriorityHeapq()
        queue.push('c', priority=0)
        queue.push('a', priority=1)
        queue.push('b', priority=2)

        self.assertEqual([(-2, 'b'), (0, 'c'), (-1, 'a')], queue.heap)

        self.assertEqual('b', queue.pop())
        self.assertEqual('a', queue.pop())
        self.assertEqual('c', queue.pop())

        self.assertEquals([], queue.heap)

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
