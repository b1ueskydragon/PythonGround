import math

# Positive integers only
digit_len = lambda k: int(math.log10(k))


def digit_to_list(given):
    ori_len = digit_len(given)
    acc = []
    for _ in reversed(range(ori_len + 1)):
        d = 10 ** digit_len(given)  # TODO math domain error when d is 0
        k = given // d
        given -= d * k
        acc.append(k)

    return acc


def is_palindrome(dist):
    ori_len = len(dist)
    pivot = math.ceil(ori_len / 2) - 1
    acc, rcc = [], []

    for i, d in enumerate(dist):
        if i > pivot:
            rcc.append(d)
        else:
            acc.append(d)

    if ori_len % 2 != 0:
        acc.pop(int(pivot))

    return acc == list(reversed(rcc))


print(is_palindrome(digit_to_list(int(input()))))
