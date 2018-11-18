def solve(ary):
    # TODO: input with pow
    ary = [_ ** 2 for _ in ary]

    for i, a in enumerate(ary, start=1):
        for b in ary[i:]:
            if (a + b) in set(ary):
                return True

    return False


given = [1, 2, 3, 4, 5, 6]  # sorted
print(solve(given))
