units = [1, 5, 10, 25]


def count_min_dp(n):
    """
     run O(n) time and space.

    :param n: make n ¢
    :return:
    """
    cache = [0 for _ in range(n + 1)]
    for u in units:
        if u < len(cache):
            cache[u] = 1

    for i in range(1, n + 1):
        '''
        e.g.
        f is result. f(n¢).

        8¢ = 1¢ + f(7¢)
        8¢ = 5¢ + f(3¢)
        '''
        # TODO migrate to for-comprehension
        var = []
        for u in units:
            if i >= u:
                var.append(1 + cache[i - u])

        cache[i] = min(var)

    return cache[n]


print(count_min_dp(n=int(input())))
