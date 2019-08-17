import math

# Positive integers only + lambda
digit = lambda k: int(math.log10(k)) + 1 if k > 0 else 1


# Recursion
def digit_rec(k):
    k = abs(k)
    if k < 10:
        return 1

    return 1 + digit_rec(k // 10)


# Big integer
def digit_big(k):
    if k is 0:
        return 1

    k = abs(k)

    if k <= 999999999999997:
        return math.floor(math.log10(k)) + 1

    count = 0
    while k:
        count += 1
        k //= 10
    return count


given = 999999999999999999999
print(digit(given))
print(digit_rec(given))
print(digit_big(-given))
