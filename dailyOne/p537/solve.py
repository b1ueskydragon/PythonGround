def collatzSeq(n):
    yield n
    while n > 1:
        if n % 2 == 0:
            yield n // 2
            n //= 2
        else:
            yield 3 * n + 1
            n = 3 * n + 1


def longest_seq(limit=1_000_000):
    cache = [0] * (limit + 1)  # 0 th is a sentinel. 1 MB at most.
    cache[1] = 1  # cache the length of n-th. it helps remove the calculation that happens before.
    for n in range(2, limit + 1):
        x = n
        count = 0
        while x >= n:  # if the next is smaller then itself, stop calculating and find from the cache.
            if x % 2 == 0:
                x //= 2
            else:
                x = 3 * x + 1
            count += 1
        cache[n] = count + cache[x]
    return cache
