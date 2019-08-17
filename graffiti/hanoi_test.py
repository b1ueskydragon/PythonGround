import unittest
from graffiti.hanoi import move


class HanoiTest(unittest.TestCase):

    def test_move(self):
        disks = 3
        expected = ['left -> middle',
                    'left -> right',
                    'middle -> right',
                    'left -> middle',
                    'right -> left',
                    'right -> middle',
                    'left -> middle']
        actual = move(disks)

        self.assertEqual(expected, actual)
