def solve():
    """ O(N^2) """
    ary = sorted(list(map(lambda k: int(k) ** 2, input().split())))
    ary.append(-1)  # sentinel

    for c in reversed(range(2, len(ary))):
        """
        Init position:
          [h, i, j, k, l, m, n]
           a              b  c 
        """
        a, b = 0, c - 1

        while a < b:
            if ary[a] + ary[b] == ary[c]:
                return True
            elif ary[a] + ary[b] < ary[c]:
                a += 1
            else:
                b -= 1

    return False


print(solve())
