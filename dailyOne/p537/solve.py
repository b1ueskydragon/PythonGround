def collatzSeq(n):
    yield n
    while n > 1:
        if n % 2 == 0:
            yield n // 2
            n //= 2
        else:
            yield 3 * n + 1
            n = 3 * n + 1


# def longest_seq(limit=1_000_000):
#     start = [0] * (limit + 1)  # sentinel
#     cache = [0] * (limit + 1)  # sentinel
#     cache[0], cache[1] = 1, 1
#     start[0], start[1] = 1, 1
#     for n in range(2, limit + 1):
#         count = 0
#         x = n
#         while x > 1:
#             if x % 2 == 0:
#                 x = x // 2
#             else:
#                 x = 3 * x + 1
#             count += 1
#             if x == start[n - 2]:
#                 cache[n] = count + cache[n - 2]
#                 start[n] = n
#                 continue
#     return cache
