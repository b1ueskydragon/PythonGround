import base64
import unittest

from dailyOne.p381.solve import Base64Convert


class Base64ConvertTest(unittest.TestCase):
    def test_32bit(self):
        converter = Base64Convert()
        string_hex: str = 'deadbeef'
        expected: str = base64.b64encode(b'\xde\xad\xbe\xef').decode()
        self.assertEqual(expected, converter.convert(string_hex))

    def test_right_just_24bit(self):
        converter = Base64Convert()
        # ASCII  M         a          n
        # Octets 77 (0x4d) 97 (0x61)  110 (0x6e)
        string_hex: str = '4d616e'
        expected: str = base64.b64encode(b'\x4d\x61\x6e').decode()
        self.assertEqual(expected, converter.convert(string_hex))

    def test_right_just_18bit(self):  # TODO
        converter = Base64Convert()
        # ASCII  M         a
        # Octets 77 (0x4d) 97 (0x61)
        string_hex: str = '4d61'
        expected: str = base64.b64encode(b'\x4d\x61').decode()
        self.assertEqual(expected, converter.convert(string_hex))
