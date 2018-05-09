def division(a, b):
    n = 0
    while a >= b:
        a -= b
        n += 1
    return n


# TODO Next step: Calc with Binary (shift operation)
# 28 / 5 = 5 ..
# 5 x 5 + 3 = 28
# Q = 5
print(5 << 2)  # 5 x 2^2 = 20
print(2 ** 2 + division(28 - (5 << 2), 5))

print(28 >> 2)  # 2^2 < 5 < 2^3

# goal ?
