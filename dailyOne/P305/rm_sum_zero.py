def solve(lst):
    # jump to next head. not necessary remove elements.
    acc = 0
    head = 0
    i = head + 1

    if lst[head] == 0:
        return lst[head + 1:]

    while i < len(lst):
        acc += lst[i]
        i += 1
        if acc == 0 or acc == lst[head]:
            return [lst[head]] + lst[i:]

    return lst


# linked list
given = [3, 4, -7, 5, -6, 6]
given00 = [5, -6, 6, 7]

# print(solve(given))  # 5
# print(solve(given00))  # 5, 7

given01 = [0, 4, -7, 7, 3, 8]
print(solve(given01))  # 4, 3, 8

given02 = [4, -7, 7, 3, -3, -8, -10]
print(solve(given02))  # 4, -8, -10
