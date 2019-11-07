"""
(i) 0, 1, 2, 3, 4, 5, 6,  7  ..
(v) 1, 1, 2, 3, 5, 8, 13, 21 ..
"""


def fib_rec(n):
    if n <= 1:
        return 1
    return fib_rec(n - 2) + fib_rec(n - 1)


def fib_tail_rec(prev, n):
    # TODO
    # make branch to be created on linear
    if n == 1:
        return n
    return fib_tail_rec(n, prev + n)


def fib_memo(n):
    # TODO
    return


def fib_dp(n):
    fibs = {0: 1, 1: 1}
    # TODO
    return fibs


if __name__ == '__main__':
    n = 10
    print([fib_rec(i) for i in range(n)])
    print([fib_tail_rec(1, i) for i in range(n)])
