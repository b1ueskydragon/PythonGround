from unittest import TestCase

from .fib_and_fib import *


class FibAndFibTest(TestCase):
    def test_fib_rec(self):
        under_test = FibRec()
        self.assertEqual(1, under_test.fib(0))
        self.assertEqual(377, under_test.fib(13))

    def test_fib_tailrec(self):
        under_test = FibTailRecLike()
        self.assertEqual(1, under_test.fib(0))
        self.assertEqual(377, under_test.fib(13))

    def test_fib_loop(self):
        under_test = FibLoop()
        self.assertEqual(1, under_test.fib(0))
        self.assertEqual(377, under_test.fib(13))

    def test_fib_linear(self):
        under_test = FibLinear(13)
        self.assertEqual([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], under_test.fib())
