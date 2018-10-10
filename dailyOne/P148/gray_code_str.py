def gray_code_str(binary: int):
    digits = str(binary)

    """ high to low """
    prev = digits[0]

    """ 
    1 ^ 0 == 1, 0 ^ 0 == 0
      0 case that make an XOR with right shifted num (high order digit should be `0`)
    """
    output = digits[0]
    i = 1
    while i != len(digits):
        output += xor(prev, digits[i])
        prev = digits[i]
        i += 1

    return output


xor = lambda a, b: "0" if a == b else "1"

print(gray_code_str(1011))
