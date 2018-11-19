def solve():
    ary = sorted([int(input()) ** 2 for _ in range(int(input()))])
    print(ary)

    for i, a in enumerate(ary, start=1):
        for b in ary[i:]:
            if (a + b) in set(ary):
                return True

    return False


# given = [1, 2, 3, 4, 5, 6]  # sorted
print(solve())
