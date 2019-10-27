import unittest
from w3resource.pick3 import pick3th, pick3th_another


class Pick3Test(unittest.TestCase):
    def test_pick3th_nums(self):
        nums = [10 * i for i in range(1, 10)]
        self.assertEqual([30, 60, 90, 40, 80, 50, 20, 70, 10], pick3th(nums))
        self.assertEqual([], nums)

    def test_pick3th_another_nums(self):
        nums = [10 * i for i in range(1, 10)]
        self.assertEqual([30, 60, 90, 40, 80, 50, 20, 70, 10], pick3th_another(nums))
        self.assertEqual([], nums)

    def test_pick3th_alphas(self):
        alphas = [chr(i) for i in range(97, 123)]
        self.assertEqual(
            ['c', 'f', 'i', 'l', 'o', 'r', 'u', 'x', 'a', 'e', 'j', 'n', 's', 'w', 'b', 'h', 'p', 'v', 'd', 'm', 'y',
             'k', 'z', 't', 'g', 'q']
            , pick3th(alphas))
        self.assertEqual([], alphas)

    def test_pick3th_another_alphas(self):
        alphas = [chr(i) for i in range(97, 123)]

        self.assertEqual(
            ['c', 'f', 'i', 'l', 'o', 'r', 'u', 'x', 'a', 'e', 'j', 'n', 's', 'w', 'b', 'h', 'p', 'v', 'd', 'm', 'y',
             'k', 'z', 't', 'g', 'q']
            , pick3th_another(alphas))
        self.assertEqual([], alphas)


if __name__ == '__main__':
    unittest.main()
