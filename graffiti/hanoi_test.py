import unittest
from graffiti.hanoi import move


class HanoiTest(unittest.TestCase):

    def test_move(self):
        disks = 3
        expected = ['1, left -> middle',
                    '2, left -> right',
                    '1, middle -> right',
                    '3, left -> middle',
                    '1, right -> left',
                    '2, right -> middle',
                    '1, left -> middle']
        actual = move(disks)

        self.assertEqual(expected, actual)
