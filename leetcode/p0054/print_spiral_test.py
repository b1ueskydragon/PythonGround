from unittest import TestCase

from .solve import Solution as A


class SpiralMatrixTest(TestCase):
    def test_spiral_order_4x5(self):
        a = A()
        matrix = [[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]]
        self.assertEqual(
            [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12],
            a.spiralOrder(matrix))

    def test_spiral_order_3x3(self):
        a = A()
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
            a.spiralOrder(matrix))

    def test_spiral_order_3x4(self):
        a = A()
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        self.assertEqual(
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            a.spiralOrder(matrix))

    def test_spiral_order_1x1(self):
        a = A()
        matrix = [[99]]
        self.assertEqual([99], a.spiralOrder(matrix))

    def test_spiral_order_24x4(self):
        a = A()
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        self.assertEqual(
            [1, 2, 3, 4, 8, 12, 4, 8, 12, 4, 8, 12, 4, 8, 12, 4, 8, 12, 4, 8, 12, 4, 8, 12, 4, 8, 12, 11, 10, 9, 5, 1,
             9, 5, 1, 9, 5, 1, 9, 5, 1, 9, 5, 1, 9, 5, 1, 9, 5, 1, 9, 5, 6, 7, 11, 3, 7, 11, 3, 7, 11, 3, 7, 11, 3, 7,
             11, 3, 7, 11, 3, 7, 11, 3, 7, 6, 2, 10, 6, 2, 10, 6, 2, 10, 6, 2, 10, 6, 2, 10, 6, 2, 10, 6, 2, 10],
            a.spiralOrder(matrix))

    def test_spiral_order_empty(self):
        a = A()
        matrix = [[]]
        self.assertEqual([], a.spiralOrder(matrix))

    def test_spiral_order_empty_list(self):
        a = A()
        matrix = []
        self.assertEqual([], a.spiralOrder(matrix))

    def test_spiral_order_23x1(self):
        a = A()
        matrix = [[1], [0], [2], [3], [1], [0], [2], [3], [1], [0], [2], [3], [1], [0], [2], [3], [1], [0], [2], [3],
                  [4], [0], [-9]]
        self.assertEqual([1, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 4, 0, -9], a.spiralOrder(matrix))

    def test_spiral_order_1x3(self):
        a = A()
        matrix = [[1, 2, 3]]
        self.assertEqual([1, 2, 3], a.spiralOrder(matrix))
