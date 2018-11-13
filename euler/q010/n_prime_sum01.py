def solve(n=2_000_000, cache=0):
    # if n < 2:
    #     return 0
    # if n == 2:
    #     return 2
    # if n % 2 == 0:
    #     n += 1

    primes = [True] * n
    primes[0], primes[1] = [None] * 2  # sentinels

    for i, prime in enumerate(primes):
        if not prime:
            continue  # skip

        elif prime and i <= n ** 0.5 + 1:
            primes[i * 2::i] = [False] * (((n - 1) // i) - 1)

        cache += i

    print(cache)


solve()
