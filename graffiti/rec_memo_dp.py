"""
(i) 0, 1, 2, 3, 4, 5, 6,  7  ..
(v) 1, 1, 2, 3, 5, 8, 13, 21 ..
"""


def fib_rec(n):
    """
    top-down approach.
    n, n-1, n-2 ...

             n
           /   \
       n-1    n-2
       / \     / \
     n-2 n-3 n-4 n-3
           ...

    calling same number and this means calc same thing again.

    :param n:
    :return:
    """
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
    """
    Bottom-up approach (write recursion iteratively).
    0, 1, ... , n

    :param n:
    :return:
    """
    fibs = {0: 1, 1: 1}
    for i in range(2, n):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs


if __name__ == '__main__':
    n = 10
    print([fib_rec(i) for i in range(n)])
    print(list(fib_dp(n).values()))
