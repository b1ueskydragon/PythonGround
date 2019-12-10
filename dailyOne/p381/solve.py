"""
Implement a function that converts a hex string to base64.

see also: https://en.wikipedia.org/wiki/Base64
"""


class Base64Convert:
    def __init__(self):
        self.table = Base64Convert._get_table()
        self.padding_symbol = '='

    @staticmethod
    def _get_table():
        """
        00 : 000000 A ~ 25 : 011001 Z
        26 : 011010 a ~ 51 : 110011 z
        52 : 110100 0 ~ 61 : 111101 9
        62 : 111110 +
        63 : 111111 /

        padding : =
        """
        table = {}
        for i in range(0, 26):
            table[i] = chr(i + 65)
        for i in range(26, 52):
            table[i] = chr(i + 71)
        for i in range(0, 10):
            table[i + 52] = str(i)
        table[62] = '+'
        table[63] = '/'
        return table

    @staticmethod
    def _padding(lower_sextets: str):
        sextets = int(lower_sextets, 2)
        while sextets < 63:
            sextets <<= 1
        if sextets > 63:
            sextets >>= 1
        return sextets

    def convert(self, string_hex: str):
        """
        1101\1110\1010\1101\1011\1110\1110\1111
         d    e    a    d    b    e    e    f
        110111\101010\110110\111110\111011\11 00 00
         3      q       2      +     7      w  =  =   # padding
        """
        hex_int = int(string_hex, 16)
        bin_int = bin(hex_int)[2:]

        # zero fill
        if len(bin_int) % 8 != 0:
            total_octets_len = ((len(bin_int) // 8) + 1) * 8
            bin_int = bin_int.rjust(total_octets_len, '0')

        table = self.table
        res = ''
        i = 0
        embedding = ''
        while i < len(bin_int):
            sextets = bin_int[i:i + 6]
            if len(sextets) < 6:
                # only the least significant chunk can reach the block.
                embedding = (self.padding_symbol * ((6 - len(sextets)) // 2))
                sextets = bin(Base64Convert._padding(sextets))
            res += table[int(str(sextets), 2)]
            i += 6
        res += embedding
        return res
