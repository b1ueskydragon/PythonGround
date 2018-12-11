def solve(lst):
    # jump to next head. not necessary remove elements.
    head = 0
    acc = 0

    for i, v in enumerate(lst):
        acc += v
        if acc == 0:
            head = i + 1
            break

    return lst[head:]


# linked list
given = [3, 4, -7, 5, -6, 6]
given01 = [0, 4, -7, 7, 3]
print(solve(given))  # 5
print(solve(given01))  # 4, 3
