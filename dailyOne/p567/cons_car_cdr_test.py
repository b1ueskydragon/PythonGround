import unittest
from .cons_car_cdr import *


class ConsCarCdrTest(unittest.TestCase):
    def test_car(self):
        pair = cons('a', 'b')
        self.assertEqual(car(pair), 'a')

    def test_cdr(self):
        pair = cons('a', 'b')
        self.assertEqual(cdr(pair), 'b')
