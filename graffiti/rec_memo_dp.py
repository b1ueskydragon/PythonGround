"""
(i) 0, 1, 2, 3, 4, 5, 6,  7  ..
(v) 1, 1, 2, 3, 5, 8, 13, 21 ..
"""


def fib_rec_slow(n):
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
    very slow.

    :param n:
    :return:
    """
    if n <= 1:
        return 1
    return fib_rec_slow(n - 2) + fib_rec_slow(n - 1)


memo = {}  # global


def fib_memo(n):
    """
    Do not calc again that has been calculated.

    :param n:
    :return:
    """
    if n in memo:
        # prevent to re-call to the same params again.
        return memo[n]
    if n <= 1:
        memo[n] = 1
        return 1
    memo[n] = fib_memo(n - 2) + fib_memo(n - 1)
    return memo[n]


def fib_tail_linear_rec(n, prev=1, res=1):
    # make branch to be created on linear
    if n <= 1:
        return res
    return fib_tail_linear_rec(n - 1, res, res + prev)


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
    # TODO measure speed or plot to graph
    n = int(input())
    # print([fib_rec_slow(i) for i in range(n)])
    fib_memo(n - 1)
    print(list(memo.values()))
    print([fib_tail_linear_rec(i) for i in range(n)])
    print(list(fib_dp(n).values()))
