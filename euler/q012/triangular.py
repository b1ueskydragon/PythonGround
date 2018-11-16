import time

"""
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""

min_count = 500


def count(num, cnt=0):
    if num == 1:
        return 1

    for i in range(1, num):
        if i == num ** 0.5:
            return cnt * 2 + 1
        if i > num ** 0.5:
            return cnt * 2
        if num % i == 0:
            cnt += 1
    return cnt * 2


def solve(num=1, acc=1, r=min_count):
    while count(num) < r:
        acc += 1
        num += acc

    return num


st = time.time()
print(solve())  # 12375 * (12375 + 1) / 2 = 76576500
ed = time.time()
print(f'{ed - st} sec')
