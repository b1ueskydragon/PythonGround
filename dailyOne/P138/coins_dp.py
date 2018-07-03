units = [1, 5, 10, 25]


def count_min_dp(n):
    """
     run O(n) time and space.

    :param n: make n ¢
    :return:
    """
    memoied = [0 for _ in range(n + 1)]  # cache
    for u in units:
        if u < len(memoied):
            memoied[u] = 1

    for i in range(1, n + 1):
        '''
        e.g.
        f is result. f(n¢).

        8¢ = 1¢ + f(7¢)
        8¢ = 5¢ + f(3¢)
        
        candidate of memoied[i] = unit + f(i - unit)
        '''
        # TODO migrate to for-comprehension
        results = []
        '''use cache in O(n)'''
        for u in units:
            if i >= u:
                results.append(1 + memoied[i - u])

        memoied[i] = min(results)

    return memoied[n]


print(count_min_dp(n=int(input())))
