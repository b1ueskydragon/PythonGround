class Codec:
    """
    string to be encoded have no digits and consists solely of alphabetic characters.
    string to be decoded is valid.
    """

    def encode_str(self, string):
        if not string: return ''
        bef = string[0]
        buffer = ''
        count = 1
        for i in range(1, len(string)):
            curr = string[i]
            if curr == bef:
                count += 1
            else:
                buffer += str(count) + bef
                count = 1  # reset
                bef = curr  # reset
        buffer += str(count) + bef  # flush
        return buffer

    def decode_str(self, encoded):
        if not encoded: return ''
        buffer = ''
        digits = 0
        for x in encoded:
            if str.isnumeric(x):
                digits = digits * 10 + int(x)
            else:
                buffer += digits * x
                digits = 0  # reset
        return buffer
