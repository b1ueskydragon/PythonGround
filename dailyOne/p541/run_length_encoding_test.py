import unittest

from .run_length_encoding import Codec


class StringEncodeDecodeCase(unittest.TestCase):
    def test_emtpy(self):
        codec = Codec()
        self.assertEqual('', codec.encode_str(''))

    def test_one_digit(self):
        codec = Codec()
        str = "AAAABBBCCDAA"
        expected = "4A3B2C1D2A"
        self.assertEqual(expected, codec.encode_str(str))

    def test_has_large_digits(self):
        codec = Codec()
        str = "A" * 3 + "B" * 123 + "X" * 10
        expected = "3A123B10X"
        self.assertEqual(expected, codec.encode_str(str))

    def test_decode_one_digit(self):
        codec = Codec()
        str = "AAAABBBCCDAA"
        self.assertEqual(str, codec.decode_str(codec.encode_str(str)))

    def test_decode_has_large_digits(self):
        codec = Codec()
        str = "A" * 3 + "B" * 123 + "X" * 10
        self.assertEqual(str, codec.decode_str(codec.encode_str(str)))
