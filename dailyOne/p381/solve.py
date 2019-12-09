"""
Implement a function that converts a hex string to base64.
Base64 is meant to encode bytes (8 bit).

see also: https://en.wikipedia.org/wiki/Base64
"""

import base64

# fundamental usage
hex_string = b'\xde\xad\xbe\xef'
byte_array = b'3q2+7w=='

print(base64.b64encode(hex_string))
print(base64.b64decode(byte_array))

hex_int = int('deadbeef', 16)
print(hex_int)
print(bin(hex_int))
# 1101\1110\1010\1101\1011\1110\1110\1111
#   d    e    a    d    b    e    e    f
# 110111\101010\110110\111110\111011\11 00 00
#   3      q       2      +     7     w  =  =   # padding
