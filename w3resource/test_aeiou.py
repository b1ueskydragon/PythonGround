import unittest

from w3resource.aeiou import permutation, permutation_builtin


class AeiouTest(unittest.TestCase):
    def test_permutation_empty_xs(self):
        vowels = []
        self.assertEqual(permutation(vowels), permutation_builtin(vowels))

    def test_permutation_single_element(self):
        vowels = ['a']
        self.assertEqual(permutation(vowels), permutation_builtin(vowels))

    def test_permutation(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        self.assertEqual(permutation(vowels), permutation_builtin(vowels))


if __name__ == '__main__':
    unittest.main()
