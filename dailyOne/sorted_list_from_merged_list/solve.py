k = 3  # k sorted lists
n = 3  # each with size n


# using memory
def solve(lst):
    res = []
    for ni in range(n):
        ki = 0
        while ki < k:
            res.append(lst[ki][ni])
            ki += 1

    return res


given = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
print(solve(given))
